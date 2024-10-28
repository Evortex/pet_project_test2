import datetime
import random

import uvicorn
from fastapi import FastAPI
from alembic import command
from alembic.config import Config

from database import SessionLocal
from models.project import Project


# Функция создания экземпляра приложения FastAPI.
def create_app():
    # Создаем экземпляр приложения FastAPI.
    app = FastAPI()

    # Инициализируем конфигурацию alembic.
    alembic_cfg = Config("alembic.ini")
    # Применяем миграции к БД (обычно это делается вручную).
    command.upgrade(alembic_cfg, "head")

    # Возвращаем экземпляр приложения.
    return app


# Присваиваем глобальной переменной app экземпляр приложения.
app = create_app()


# Оператор события startup, который будет выполнять метод при запуске приложения.
@app.on_event("startup")
# Функция для сохранения нового проекта в БД и вывода списка всех проектов.
def save_to_db_and_read():
    # Создаем локальную сессию для работы с БД.
    db = SessionLocal()

    # Создаем экземпляр класса Project.
    project = Project(name="Тестовый проект " + str(random.randint(0, 9999)), description="Описание проекта",
                      author="Автор", created_at=datetime.date.today().strftime("%B %d, %Y"))

    # Выводим информацию о проекте.
    print("Сохранение нового проекта в базу данных: " + project.name + " "
          + project.description + " " + project.author + " " + project.created_at + "\n")

    # Пытаемся выполнить код в блоке try.
    try:
        # Добавляем экземпляр класса Project в сессию.
        db.add(project)
        # Коммитим изменения в БД.
        db.commit()
        # Обновляем экземпляр класса Project.
        db.refresh(project)
    except Exception as e:
        # Если произошла ошибка, выводим ее в консоль.
        print("Ошибка: " + e)

    # Получаем все проекты из БД, используя метод query().all().
    projects = db.query(Project).all()

    # Выводим списков всех проектов, хранящихся в БД.
    print("Список сохраненных проектов в базе данных: ")
    for project in projects:
        print(project.name)


# Оператор запуска приложения.
if __name__ == '__main__':
    # Запуск сервера uvicorn из приложения app, по адресу 0.0.0.0:8080,
    # с автоматической перезагрузкой при изменении кода и 3 воркерами.
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True, workers=3)
