from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.sql.schema import MetaData
from starlette.requests import Request

from application.database import Base
from application.exceptions import CustomException
from application.questions.views import router as router_questions
from application.settings import settings


def init_routers(app_: FastAPI) -> None:
    """Ручки должны быть отдельным файлом, но по скольку их мало не будем заморачиваться."""
    app_.include_router(
        router_questions,
        prefix=f"{settings.API_V1_STR}/questions",
        tags=["questions"],
    )


def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="task_for_bewise",
        description="Тестовое задание для bewise",
        version="0.0.1",
        openapi_url=f"{settings.API_V1_STR}/docs/openapi.json",
        redoc_url=f"{settings.API_V1_STR}/docs",
        contact={
            "name": "Смелов Илья",
            "url": "https://github.com/PivnoyFei",
        },
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_


app: FastAPI = create_app()
metadata: MetaData = Base.metadata
