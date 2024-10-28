import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


# Модель(сущность базы данных) Project, которая наследуется от класса Base.
class Project(Base):

# Указываем соответствующее имя таблицы в БД.
    __tablename__ = 'projects'

    # Декларируем столбцы в таблице.
    # Начало (пиши код внутри комментария)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    author = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    # Конец
