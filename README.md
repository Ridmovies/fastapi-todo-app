# FastAPI ToDo List

Todo приложение
![Screenshot from 2025-05-06 10-50-15.png](Screenshot%20from%202025-05-06%2010-50-15.png)
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
- [x] Jinja2 frontend


#### Запуск приложения
```bash
uvicorn src.main:app --port 8000 --reload
```

#### Документация:
http://127.0.0.1:8000/docs


## Полезные ссылки:
FastAPI Best Practices:
https://github.com/zhanymkanov/fastapi-best-practices

Database:
https://fastapi.tiangolo.com/tutorial/sql-databases/

Settings Management:
https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage

Alembic 1.14.1 documentation:
https://alembic.sqlalchemy.org/en/latest/tutorial.html