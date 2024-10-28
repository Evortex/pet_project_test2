import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


# Модель(сущность базы данных) Project, которая наследуется от класса Base.
class Project(Base):
    # Указываем соответствующее имя таблицы в БД.
    __tablename__ = 'projects'

    # Декларируем столбцы в таблице.
    id = Column(Integer, primary_key=True, index=True)  # Число, первичный ключ, индекс.
    name = Column(String, unique=True)  # Строка, уникальное значение.
    description = Column(String)
    author = Column(String)
    # Дата и время создания проекта, по умолчанию - текущие.
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
