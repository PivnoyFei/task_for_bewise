FROM python:3.11.0-slim

WORKDIR /srv/www/app

COPY . .

COPY pyproject.toml poetry.lock ./
# RUN apt-get update && apt-get install gcc libpq-dev -y
# RUN pip install --no-cache-dir --upgrade pip \
#     && pip install -r requirements.txt

COPY . ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install -n --no-interaction --no-ansi --no-dev

# CMD ["uvicorn", "application.main:app", "--reload", "--host", "0.0.0.0"]