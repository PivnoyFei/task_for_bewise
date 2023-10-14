from sqlalchemy import insert, select

from application.database import db_redis, get_session
from application.questions.models import Question
from application.questions.schemas import QuestionOut
from application.questions.utils import get_questions


class QuestionManager:
    mpdel = Question

    async def checking_list_questions(self, questions: list[QuestionOut]) -> dict | None:
        """
        Делает первый запрос в базу на проверку наличия в ней.
        Второй делает запись, возвращает последний вопрос.
        Выдает предыдущий сохраненный вопрос и записывает последний в `redis`.
        """
        set_questions = {question.id for question in questions}
        async with get_session() as session:
            while set_questions:
                query = await session.execute(
                    select(self.mpdel.id).filter(self.mpdel.id.in_(set_questions))
                )
                query = query.all()
                if not query:
                    break

                query_set = {question.id for question in query}

                # оставляем в списке `questions` только вопросы которых нет в нашей базе
                questions: list[QuestionOut] = [
                    question for question in questions if question.id not in query_set
                ]

                # получаем нужное количество новых вопросов
                new_questions: list[QuestionOut] = await get_questions(len(query))

                # обновляем `set_questions` что бы не повторять запросы в базу
                set_questions = {question.id for question in new_questions}

                questions.extend(questions)

            await session.execute(
                insert(self.mpdel).values([question.to_dict() for question in questions])
            )
            await session.commit()

            last_question: dict = db_redis.hgetall("last_question")
            db_redis.hset("last_question", mapping=questions[-1].redis_dict())
            return last_question or None
