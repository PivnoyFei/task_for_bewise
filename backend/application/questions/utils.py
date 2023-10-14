import requests

from application.exceptions import BadRequestException
from application.questions.schemas import QuestionOut
from application.settings import settings


async def get_questions(count: int | None = 1) -> list[QuestionOut]:
    response = requests.get(settings.SERVICE_URL, params={"count": count})
    if response.status_code != 200:
        raise BadRequestException("Нет ответа от API сервиса")
    return [QuestionOut(**question) for question in response.json()]
