from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from application.questions.managers import QuestionManager
from application.questions.schemas import LastQuestion, QuestionPath
from application.questions.utils import get_questions

router = APIRouter()


@router.get("/", response_model=LastQuestion | None, status_code=HTTP_200_OK)
async def get_question(questions_num: QuestionPath) -> LastQuestion | None:
    if questions := await get_questions(questions_num):
        return await QuestionManager().checking_list_questions(questions)
