from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
engine = create_engine("sqlite:///database.db")
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class E95(Base):
    __tablename__ = "E95"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    adres: Mapped[str] = mapped_column(String(50))
    price: Mapped[str] = mapped_column(String(30))
    actual_date: Mapped[str] = mapped_column(String(30))

class LPG(Base):
    __tablename__ = "LPG"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    adres: Mapped[str] = mapped_column(String(50))
    price: Mapped[str] = mapped_column(String(30))
    actual_date: Mapped[str] = mapped_column(String(30))
class E98(Base):
    __tablename__ = "E98"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    adres: Mapped[str] = mapped_column(String(50))
    price: Mapped[str] = mapped_column(String(30))
    actual_date: Mapped[str] = mapped_column(String(30))

class ON(Base):
    __tablename__ = "ON"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    adres: Mapped[str] = mapped_column(String(50))
    price: Mapped[str] = mapped_column(String(30))
    actual_date: Mapped[str] = mapped_column(String(30))

Base.metadata.create_all(engine)