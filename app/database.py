from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Присваиваем URL для подключения к БД глобальной переменной(константе) SQLALCHEMY_URL.
SQLALCHEMY_URL = "postgresql+psycopg2://ai_creative_platform_user:5555@localhost:5432/ai_creative_platform"

# Создаем экземпляр класса Engine для подключения к БД.
engine = create_engine(SQLALCHEMY_URL)
# Собираем экземпляр класса SessionLocal для работы с сессиями, с отключенным автофлашем и автокоммитом.
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
# Создаем экземпляр класса Base для создания моделей.
Base = declarative_base()


# Функция для получения экземпляра класса SessionLocal.
def get_db():
    # Создаем локальную переменную db, которая будет хранить экземпляр класса SessionLocal.
    db = SessionLocal()

    # Пытаемся выполнить код в блоке try, в любом случае выполняем код в блоке finally.
    try:
        # Возвращаем экземпляр класса SessionLocal.
        yield db
    finally:
        # Всегда после работы закрываем соединение с БД.
        db.close()
