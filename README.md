# To-Do List

Небольшой проект для демонстрации навыков написания веб-сервера. На данный момент в проекте реализовано:

- Добавление и удаление задач
- JWT-аутентификация
- Миграции PostgreSQL

---

## Технологии

- Python 3.10
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- Alembic

---

## Запуск


### Инструкция
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/diemensa/fastapi_project
   cd fastapi_project
2. Собрать и запустить БД при помощи docker-compose:
   ```bash
   docker-compose up --build
3. Применить миграции
   ```bash
   alembic revision --autogenerate -m 'Initial commit'
   ```
   
   ```bash
   alembic upgrade head
   ```
4. Запустить программу через main.py

### Документация API
После запуска сервиса можно открыть документацию:
- SwaggerUI: http://localhost:8080/docs
- ReDoc: http://localhost:8080/redoc
