from datetime import datetime
from typing import Annotated, Any

from fastapi import Query
from pydantic import BaseModel

QuestionPath = Annotated[int, Query(title="Ограничение по количеству вопросов", ge=1, le=10)]


class BaseShema(BaseModel):
    id: int

    class ConfigDict:
        from_attributes = True


class QuestionOut(BaseShema):
    question: str
    answer: str
    created_at: datetime

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "created_at": self.created_at.replace(tzinfo=None),
        }

    def redis_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "created_at": str(self.created_at),
        }


class LastQuestion(BaseShema):
    question: str
    answer: str
    created_at: str
