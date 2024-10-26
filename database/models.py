from sqlalchemy import Boolean, DateTime, func, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Account(Base):
    __tablename__ = 'accounts'


    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(225))
    password: Mapped[str] = mapped_column(String(225))
    free: Mapped[Boolean] = mapped_column(default=True)
    order: Mapped[str] = mapped_column(Text, nullable=True)