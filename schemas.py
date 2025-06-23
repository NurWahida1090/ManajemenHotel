from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class UserSchema(BaseModel):
    nama: str
    no_telepon: str
    email: str
    password: str
    role: str
    created_at: Optional[datetime]

class KamarSchema(BaseModel):
    nomor_kamar: str
    tipe_kamar: str
    gambar_kamar: str
    deskripsi: str
    harga: float
    status: str

class FasilitasSchema(BaseModel):
    nama_fasilitas: str
    deskripsi: str
    gambar_fasilitas: str

class ReservasiSchema(BaseModel):
    id_user: int
    id_kamar: int
    nomor_kamar: int
    tanggal_checkin: date
    tanggal_checkout: date
    status: str
    created_at: Optional[datetime]
