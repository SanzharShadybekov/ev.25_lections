# ORM (Object-Relational Mapping) - технология программирования, благодаря которой разработчики могуть использовать язык программирования для взаимодействия с реляционной базой данных(PostgreSQL, MySQL и тд), вместо того чтобы писать операторы SQL, вы будете писать код ООП на языке програмиирования. Это очень сильно ускоряет разработку приложения и бд, особенно на нчальных этапах.

from peewee import PostgresqlDatabase


db = PostgresqlDatabase(
    'orm_db1',
    user='sanzhar',
    password='1',
    host='localhost',
    port=5432
)
