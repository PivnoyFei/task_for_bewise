# task_for_bewise

### Стек:
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.11](https://img.shields.io/badge/3.11-blue?style=flat-square&logo=3.11)
![FastAPI](https://img.shields.io/badge/FastAPI-171515?style=flat-square&logo=FastAPI)![0.100](https://img.shields.io/badge/0.100-blue?style=flat-square&logo=0.100)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-171515?style=flat-square&logo=PostgreSQL)![13.0](https://img.shields.io/badge/13.0-blue?style=flat-square&logo=13.0)

![Pydantic](https://img.shields.io/badge/Pydantic-171515?style=flat-square&logo=Pydantic)![2](https://img.shields.io/badge/2-blue?style=flat-square&logo=2)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-171515?style=flat-square&logo=SQLAlchemy)![2.0](https://img.shields.io/badge/2.0-blue?style=flat-square&logo=2.0)

![Docker-compose](https://img.shields.io/badge/Docker--compose-171515?style=flat-square&logo=Docker)

### Задачи:

1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.


2. Реализовать на Python3 простой веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:
В сервисе должно быть реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  ;

```
После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.
```

3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.

4. Желательно, если при выполнении задания вы будете использовать docker-compose, SqlAalchemy,  пользоваться аннотацией типов.

### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/PivnoyFei/delibasket.git
cd delibasket
```

### Перед запуском сервера, в папке infra необходимо создать `.env` на основе `.env.template` файл со своими данными.
#### Переходим в папку с файлом docker-compose.yaml:
```bash
cd bewise-infra
```

### Запуск проекта
```bash
docker-compose up -d --build
```

#### Миграции базы данных:
```bash
# docker-compose exec bewise-backend alembic revision --message="Initial" --autogenerate
docker-compose exec bewise-backend alembic upgrade head
```

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```

#### Автор
[Смелов Илья](https://github.com/PivnoyFei)
