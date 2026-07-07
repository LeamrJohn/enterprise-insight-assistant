from sqlalchemy import String, DateTime, func
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    api_key: Mapped[str] = mapped_column(
        String(64), unique=True, nullable=False, index=True
    )
    role: Mapped[str] = mapped_column(
        String(20), nullable=False, default="user"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
