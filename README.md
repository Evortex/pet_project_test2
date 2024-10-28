# Урок 4: БД, ORM, Миграции

В этом уроке тебе предстоит научиться работать с базами данных. 
Сначала тебе потребуется развернуть PostgreSQL DB локально с помощью Docker,
затем ознакомиться с конфигурацией подключения к ней, а после самостоятельно написать
модель проекта с помощью SQLAlchemy и сгенерировать миграцию для создания соответствующей 
таблицы в базе данных инструментом Alembic.
По итогам выполнения этого урока ты сможешь полноценно работать с базами данных на уровне 
Python приложения, освоишь использование ORM паттерна и инструментов версионирования изменений 
базы данных(миграций).

## Задание:

1. Инициализируй проект, установи зависимости из Pipfile.lock автоматически с помощью PyCharm.

2. Открой на своем ПК Docker и запусти docker-compose.yml, 
чтобы развернуть PostgreSQL базу данных локально. 
PyCharm сам тебе предложит установить docker-плагин, чтобы сделать это быстрей и удобней.

3. Открой файл [database.py](app/database.py) и ознакомься с конфигурацией подключения к базе данных.

4. Открой файл [project.py](app/models/project.py), расположенный в пакете models, чтобы создать модель проекта.  
Она должна включать в себя:
    - id проекта (id);
    - название проекта (name);
    - описание проекта (description);
    - автора проекта (author);
    - дату создания проекта (created_at);  
  
    Используй типы данных Integer, String и Datetime, помни, что ID обязательно должен являться первичным ключом,
    а имя быть уникальным. [Проектирование моделей в SQLAlchemy](https://pythonru.com/biblioteki/shemy-v-sqlalchemy-orm).

5. Перейди в терминал(Alt+F12) и выполни команду, чтобы сгенерировать миграцию для базы данных.
В директории app/alemibc/version сгенерируется новый файл, описывающий изменения в структуре базы данных.
Открой его и изучи, внутри описана логика создания таблицы.
```
alembic revision --autogenerate -m "create table projects"
```

6. Открой main.py и запусти приложение, прочитай вывод в консоль и изучи код метода save_to_db_and_read.
   Он продемонстрирует сохранение проекта и чтение его из базы данных.

### Важные примечания:

1. Для того чтобы корректно начать работу зайди в настройки 
(File-->Settings-->Project-->ProjectStructure) и пометь директорию app в качестве Sources. 
Это нужно, чтобы программа могла правильно видеть файлы внутри проекта.
2. Пиши свой код только внутри отведенных областей между комментариями, 
каждая область помечена номером, соответствующим номеру задания и содержит обозначения границ ("начало" и "конец").
3. Пользуйся поисковыми системами и сервисом ChatGPT, чтобы быстрее находить решения.


###### В директории examples ты можешь найти решения заданий, но мы рекомендуем попытаться решить их самостоятельно.