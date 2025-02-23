# FastAPI ToDo List

Todo приложение

## Инструменты:
### Основной стек:
- FastAPI
- SQLAlchemy
- SQLite + aiosqlite
- 
### Дополнительные инструменты:
- FastAPI
- black
- uvicorn
- Jinja2


## Roadmap
- [x] Создание и подключение к базе данных SQLite
- [x] Модель Todo
- [x] Todo роутер
- [ ] Jinja2 frontend
  - [ ] подключить Jinja2

#### Запуск приложения
```bash
uvicorn src.main:app --port 8000 --reload
```

#### Документация:
http://127.0.0.1:8000/docs


## DEVELOP
## Alembic
Изменить настройки env.py
```
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
target_metadata = Base.metadata
```


### Creating async an Environment
```bash
alembic init --template async alembic
```

### Generate first migration
```bash
alembic revision --autogenerate -m "initial migration"
```

### Apply generated migration to the database:
```bash
alembic upgrade head
```

### Rolls back the last applied migration.
```bash
alembic downgrade -1
```




## Полезные ссылки:
FastAPI Best Practices:
https://github.com/zhanymkanov/fastapi-best-practices

Database:
https://fastapi.tiangolo.com/tutorial/sql-databases/

Settings Management:
https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage

Alembic 1.14.1 documentation:
https://alembic.sqlalchemy.org/en/latest/tutorial.html