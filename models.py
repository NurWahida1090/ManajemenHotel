from sqlalchemy import Column, Integer, String, Text, DECIMAL, Date, TIMESTAMP, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(100))
    no_telepon = Column(String(20))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    role = Column(String(20))
    created_at = Column(TIMESTAMP)

class Kamar(Base):
    __tablename__ = "kamar"
    id = Column(Integer, primary_key=True, index=True)
    nomor_kamar = Column(String(20))
    tipe_kamar = Column(String(50))
    gambar_kamar = Column(String(255))
    deskripsi = Column(Text)
    harga = Column(DECIMAL)
    status = Column(String(20))

class Fasilitas(Base):
    __tablename__ = "fasilitas"
    id = Column(Integer, primary_key=True, index=True)
    nama_fasilitas = Column(String(100))
    deskripsi = Column(Text)
    gambar_fasilitas = Column(String(255))

class Reservasi(Base):
    __tablename__ = "reservasi"
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    id_kamar = Column(Integer, ForeignKey("kamar.id"))
    nomor_kamar = Column(Integer)
    tanggal_checkin = Column(Date)
    tanggal_checkout = Column(Date)
    status = Column(String(20))
    created_at = Column(TIMESTAMP)
