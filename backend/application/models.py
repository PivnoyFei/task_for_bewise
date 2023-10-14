from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
