from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

from database import SessionLocal, engine
import models, schemas

from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import Form
from fastapi.responses import RedirectResponse
import re

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SECRET_KEY = "ganti_secret_key_anda"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        scheme, _, param = token.partition(" ")
        if scheme.lower() != "bearer":
            raise credentials_exception
        payload = jwt.decode(param, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user

def get_current_role(role: str):
    def role_dependency(current_user: models.User = Depends(get_current_user)):
        if current_user.role != role:
            raise HTTPException(status_code=403, detail=f"Only {role} can access this endpoint")
        return current_user
    return role_dependency

get_current_tamu = get_current_role("tamu")
get_current_admin = get_current_role("admin")

@app.post("/users")
def create_user_from_form(
    nama: str = Form(...),
    no_telepon: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    role: str = Form("tamu"), 
    db: Session = Depends(get_db),
    request: Request = None
):
    # Validasi semua field
    if not all([nama.strip(), no_telepon.strip(), email.strip(), password.strip()]):
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Semua field wajib diisi."
        })

    # Validasi nomor telepon
    if not no_telepon.isdigit() or len(no_telepon) < 8:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Nomor telepon harus berupa angka dan minimal 8 digit."
        })

    # Validasi email harus @gmail.com
    if not re.match(r"^[\w\.-]+@gmail\.com$", email):
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Email harus menggunakan domain @gmail.com."
        })
    
     # Validasi panjang password minimal 4 karakter
    if len(password) < 4:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Password minimal 4 karakter."
        })

    hashed_password = get_password_hash(password)
    db_user = models.User(
        nama=nama,
        no_telepon=no_telepon,
        email=email,
        password=hashed_password,
        role=role,
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    response = RedirectResponse(url="/", status_code=303)
    return response


@app.post("/login")
def login(
    request: Request,
    db: Session = Depends(get_db),
    username: str = Form(...),
    password: str = Form(...)
):
    if not username.strip() or not password.strip():
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Email dan password wajib diisi."
        })

    user = db.query(models.User).filter(models.User.email == username).first()
    if not user or not verify_password(password, user.password):
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Email atau password salah"
        })

    access_token = create_access_token(data={"sub": user.email})

    response = RedirectResponse(
    url="/admin/dashboard" if user.role == "admin" else "/user/dashboard",
    status_code=303
    )
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response


# ========== ADMIN ROUTES ==========
@app.get("/admin/users", response_class=HTMLResponse)
def admin_users(request: Request, db: Session = Depends(get_db), user: models.User = Depends(get_current_admin)):
    users = db.query(models.User).all()
    return templates.TemplateResponse("admin_users.html", {
        "request": request,
        "users": users
    })

@app.post("/admin/users/{id}")
async def update_user_form(
    id: int,
    request: Request,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin)
):
    form = await request.form()
    if form.get("_method") == "put":
        db_user = db.query(models.User).get(id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db_user.nama = form["nama"]
        db_user.email = form["email"]
        db_user.role = form["role"]
        db.commit()
    return RedirectResponse(url="/admin/users", status_code=303)

@app.get("/admin/users/{id}/delete")
def delete_user_form(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_admin)):
    db_user = db.query(models.User).get(id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return RedirectResponse(url="/admin/users", status_code=303)



@app.get("/admin/kamar", response_class=HTMLResponse)
def admin_kamar(request: Request, db: Session = Depends(get_db), user: models.User = Depends(get_current_admin)):
    kamar = db.query(models.Kamar).all()
    return templates.TemplateResponse("admin_kamar.html", {
        "request": request,
        "kamar": kamar
    })

@app.post("/admin/kamar")
async def admin_create_kamar_form(
    nomor_kamar: str = Form(...),
    tipe_kamar: str = Form(...),
    gambar_kamar: str = Form(...),
    deskripsi: str = Form(...),
    harga: float = Form(...),
    status: str = Form(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    kamar = models.Kamar(
        nomor_kamar=nomor_kamar,
        tipe_kamar=tipe_kamar,
        gambar_kamar=gambar_kamar,
        deskripsi=deskripsi,
        harga=harga,
        status=status
    )
    db.add(kamar)
    db.commit()
    return RedirectResponse(url="/admin/kamar", status_code=303)

@app.post("/admin/kamar/{id}")
async def admin_update_kamar_form(
    id: int,
    request: Request,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    form = await request.form()
    if form.get("_method") == "put":
        kamar = db.query(models.Kamar).get(id)
        if kamar:
            kamar.nomor_kamar = form["nomor_kamar"]
            kamar.tipe_kamar = form["tipe_kamar"]
            kamar.gambar_kamar = form["gambar_kamar"]
            kamar.deskripsi = form["deskripsi"]
            kamar.harga = float(form["harga"])
            kamar.status = form["status"]
            db.commit()
    return RedirectResponse(url="/admin/kamar", status_code=303)

@app.get("/admin/kamar/{id}/delete")
def admin_delete_kamar_form(
    id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    kamar = db.query(models.Kamar).get(id)
    if kamar:
        db.delete(kamar)
        db.commit()
    return RedirectResponse(url="/admin/kamar", status_code=303)



@app.get("/admin/fasilitas", response_class=HTMLResponse)
def admin_fasilitas(request: Request, db: Session = Depends(get_db), user: models.User = Depends(get_current_admin)):
    fasilitas = db.query(models.Fasilitas).all()
    return templates.TemplateResponse("admin_fasilitas.html", {
        "request": request,
        "fasilitas": fasilitas
    })

@app.post("/admin/fasilitas")
async def admin_create_fasilitas_form(
    nama_fasilitas: str = Form(...),
    deskripsi: str = Form(...),
    gambar_fasilitas: str = Form(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    fasilitas = models.Fasilitas(
        nama_fasilitas=nama_fasilitas,
        deskripsi=deskripsi,
        gambar_fasilitas=gambar_fasilitas
    )
    db.add(fasilitas)
    db.commit()
    return RedirectResponse(url="/admin/fasilitas", status_code=303)

@app.post("/admin/fasilitas/{id}")
async def admin_update_fasilitas_form(
    id: int,
    request: Request,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    form = await request.form()
    if form.get("_method") == "put":
        fasilitas = db.query(models.Fasilitas).get(id)
        if fasilitas:
            fasilitas.nama_fasilitas = form["nama_fasilitas"]
            fasilitas.deskripsi = form["deskripsi"]
            fasilitas.gambar_fasilitas = form["gambar_fasilitas"]
            db.commit()
    return RedirectResponse(url="/admin/fasilitas", status_code=303)

@app.get("/admin/fasilitas/{id}/delete")
def admin_delete_fasilitas_form(
    id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    fasilitas = db.query(models.Fasilitas).get(id)
    if fasilitas:
        db.delete(fasilitas)
        db.commit()
    return RedirectResponse(url="/admin/fasilitas", status_code=303)



@app.get("/admin/reservasi", response_class=HTMLResponse)
def admin_reservasi(request: Request, db: Session = Depends(get_db), user: models.User = Depends(get_current_admin)):
    reservasi = db.query(models.Reservasi).all()
    return templates.TemplateResponse("admin_reservasi.html", {
        "request": request,
        "reservasi": reservasi
    })

@app.post("/admin/reservasi")
async def admin_create_reservasi_form(
    id_user: int = Form(...),
    id_kamar: int = Form(...),
    nomor_kamar: int = Form(...),
    tanggal_checkin: str = Form(...),
    tanggal_checkout: str = Form(...),
    status: str = Form(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    reservasi = models.Reservasi(
        id_user=id_user,
        id_kamar=id_kamar,
        nomor_kamar=nomor_kamar,
        tanggal_checkin=datetime.strptime(tanggal_checkin, "%Y-%m-%d"),
        tanggal_checkout=datetime.strptime(tanggal_checkout, "%Y-%m-%d"),
        status=status,
        created_at=datetime.utcnow()
    )
    db.add(reservasi)
    db.commit()
    return RedirectResponse(url="/admin/reservasi", status_code=303)

@app.post("/admin/reservasi/{id}")
async def admin_update_reservasi_form(
    id: int,
    request: Request,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    form = await request.form()
    if form.get("_method") == "put":
        reservasi = db.query(models.Reservasi).get(id)
        if reservasi:
            reservasi.id_user = int(form["id_user"])
            reservasi.id_kamar = int(form["id_kamar"])
            reservasi.nomor_kamar = int(form["nomor_kamar"])
            reservasi.tanggal_checkin = datetime.strptime(form["tanggal_checkin"], "%Y-%m-%d")
            reservasi.tanggal_checkout = datetime.strptime(form["tanggal_checkout"], "%Y-%m-%d")
            reservasi.status = form["status"]
            db.commit()
    return RedirectResponse(url="/admin/reservasi", status_code=303)

@app.get("/admin/reservasi/{id}/delete")
def admin_delete_reservasi_form(
    id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_admin)
):
    reservasi = db.query(models.Reservasi).get(id)
    if reservasi:
        db.delete(reservasi)
        db.commit()
    return RedirectResponse(url="/admin/reservasi", status_code=303)



# ========== USER - Lihat Daftar Kamar ==========
@app.get("/kamar", response_class=HTMLResponse)
def public_lihat_kamar(request: Request, db: Session = Depends(get_db)):
    kamar = db.query(models.Kamar).all()
    return templates.TemplateResponse("user_kamar.html", {
        "request": request,
        "kamar": kamar
    })

@app.get("/user/kamar", response_class=HTMLResponse)
def user_lihat_kamar(request: Request, db: Session = Depends(get_db), user: models.User = Depends(get_current_tamu)):
    kamar = db.query(models.Kamar).all()
    return templates.TemplateResponse("user_kamar.html", {
        "request": request,
        "kamar": kamar
    })

# ========== USER - Lakukan Reservasi ==========
@app.post("/user/reservasi")
def user_lakukan_reservasi(
    id_kamar: int = Form(...),
    tanggal_checkin: str = Form(...),
    tanggal_checkout: str = Form(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_tamu)
):
    kamar = db.query(models.Kamar).filter(models.Kamar.id == id_kamar).first()
    if not kamar:
        raise HTTPException(status_code=404, detail="Kamar tidak ditemukan")
    if kamar.status.lower() != "tersedia":
        raise HTTPException(status_code=400, detail="Kamar tidak tersedia untuk reservasi")

    reservasi = models.Reservasi(
        id_user=user.id,
        id_kamar=kamar.id,
        nomor_kamar=kamar.nomor_kamar,
        tanggal_checkin=datetime.strptime(tanggal_checkin, "%Y-%m-%d"),
        tanggal_checkout=datetime.strptime(tanggal_checkout, "%Y-%m-%d"),
        status="pending",
        created_at=datetime.utcnow()
    )
    kamar.status = "terisi"
    db.add(reservasi)
    db.commit()
    return RedirectResponse(url="/user/reservasi", status_code=303)

# ========== USER - Kelola Reservasi Sendiri ==========
@app.get("/user/reservasi", response_class=HTMLResponse)
def user_reservasi_dashboard(request: Request, db: Session = Depends(get_db), user: models.User = Depends(get_current_tamu)):
    reservasi = db.query(models.Reservasi).filter(models.Reservasi.id_user == user.id).all()
    return templates.TemplateResponse("user_reservasi.html", {
        "request": request,
        "reservasi": reservasi
    })

@app.post("/user/reservasi/{id}/update")
async def update_reservasi_user(
    id: int,
    request: Request,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_tamu)
):
    form = await request.form()
    reservasi = db.query(models.Reservasi).filter(models.Reservasi.id == id, models.Reservasi.id_user == user.id).first()
    if reservasi:
        reservasi.tanggal_checkin = datetime.strptime(form["tanggal_checkin"], "%Y-%m-%d")
        reservasi.tanggal_checkout = datetime.strptime(form["tanggal_checkout"], "%Y-%m-%d")
        db.commit()
    return RedirectResponse(url="/user/reservasi", status_code=303)

@app.get("/user/reservasi/{id}/batal")
def batal_reservasi_user(id: int, db: Session = Depends(get_db), user: models.User = Depends(get_current_tamu)):
    reservasi = db.query(models.Reservasi).filter(models.Reservasi.id == id, models.Reservasi.id_user == user.id).first()
    if reservasi:
        kamar = db.query(models.Kamar).get(reservasi.id_kamar)
        if kamar:
            kamar.status = "tersedia"
        db.delete(reservasi)
        db.commit()
    return RedirectResponse(url="/user/reservasi", status_code=303)




@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    fasilitas = db.query(models.Fasilitas).all()
    return templates.TemplateResponse("index.html", {"request": request, "fasilitas": fasilitas})

@app.get("/login-ui", response_class=HTMLResponse)
def login_ui(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register-ui", response_class=HTMLResponse)
def register_ui(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/user/dashboard", response_class=HTMLResponse)
def user_dashboard(request: Request, user: models.User = Depends(get_current_user)):
    return templates.TemplateResponse("user_dashboard.html", {
        "request": request,
        "user": user
    })

@app.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/admin/dashboard", response_class=HTMLResponse)
def admin_dashboard(request: Request, user: models.User = Depends(get_current_admin)):
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "user": user
    })
