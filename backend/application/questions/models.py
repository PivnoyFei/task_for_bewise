from sqlalchemy.orm import Mapped, mapped_column

from application.database import Base
from application.models import TimeStampMixin


class Question(Base, TimeStampMixin):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    question: Mapped[str]
    answer: Mapped[str]
