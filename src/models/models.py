from typing import List

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


user_achievment = Table(
    "user_achievment",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("achievment_id", ForeignKey("achievments.id"), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    language: Mapped[str] = mapped_column(nullable=False)
    achievment: Mapped[List['Achievment']] = relationship(
        secondary=user_achievment, back_populates='users')


class Achievment(Base):
    __tablename__ = 'achievments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    users: Mapped[List['User']] = relationship(
        secondary=user_achievment, back_populates='achievments')
