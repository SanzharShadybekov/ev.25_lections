# PostgresSQL - Система управления базами данных(СУБД/DBMS)
# Это ряд программ и интрументов позволяющих создовать БД, управлять ею и манипулировать данными внутри БД(CRUD).

# Postgres - Сама база данных, она объектно-реалиционная, то есть данные хранятся в виде таблиц и таблицы имеют связи между собой(relations)

# SQL (Stuctured Query language) - деклративный язык структурированных запросов, он применяется для создание и получения данных при помощи запросов в БД 

#  ---------------------------------
#  Типы полей в Postgres

# 1. Numeric types:
#         a. smallint(2 bytes) -> -32767 to 32767
#         b. integer(4 bytes) -> -2147000 to 2147000
#         c. bigint(8 bytes) -> ...
#         d. serial(4 bytes) -> auto-increment(integer, 1-2147000)
#         c. real(4 bytes) -> число с плавающей точкой, вещественное число
#         f. double precision(8 bytes) -> real но только с двойной точкой

# 2. Character types(Строковые типы):
        # a. varchar(кол-в 255) - можем указать макс кол-во символов в ручную. Если мы указали макс кол-во симв. в 50, а заполним всего 10, то остальные 40 символов остануться не заполненными, то есть пустыми
        # b. char(255) - если не заполним все символы то остальные заполняться пробелами
        # с. text - неограниченное кол-во символов

# 3. Boolean types: 
        # boolean(1 byte) -> True/False

# 4. date - календарная дата(год.месяц.день)

# 5. location - координатная точка -> (245, -12) (x, y)

# -------------------------------
# Связи между таблицами(relations):
        # 1. Один к одному(One-to-one) - Человек и паспорт
        # 2. Один ко многим(One-to-many) - Человек и банковские карты
        # 3. Много ко многим(Many-to-many) - Студенты и преподы

# Ограничения(Constraints):
        # 1. NOT NULL
        # 2. UNIQUE
        # 3. CHECK -> CHECK number > 5
        # 4. PRIMARY KEY(для установки идентификатора данных в таблице)
        # 5. FOREIGN KEY(для установки связи между таблицами)
        # 6. ON DELETE(для установки поведения при удалении данных которые были связаны) -> SET NULL, CASCADE, RESTRICT, SET DEFAULT (value)

# -----------------------------------
# ubuntu: sudo -u postgres psql -> команда для входа в постгрес через корневого пользователя postgres
# psql -> для входа в СУБД через своего юзера

# \q -> выход из СУБД

# \du -> список всех юзеров

# \l -> список всех баз данных

# \c <dbname> -> команда подключения к бд
#     \dt -> список всех таблиц в бд
#     \d <table name> -> подробная информация про таблицу

# ИМПОРТ данных при помощи файла:
# psql -U <ваш_юзер_нэйм> -d <база_данных_создайте_предварительно> -f <путь_до_файла>

# CREATE DATABASE <dbname>; -> комнада для создание базы данных

# CREATE USER <username> WITH PASSWORD <password>; -> команда для создания юзера

# ALTER USER <username> WITH SUPERUSER; -> команда для изменения статуса юзера на суперюзера

# SELECT <row/column> FROM <tablename>;
        #  * (ALL)
#   -> Команда для получения данных из таблиц

# WHERE: используется для фильтрации по полям. Будут выводится только те данные которые соответвуют условию опера WHERE
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо'

# BETWEEN: Уcловие 'между'
# SELECT * FROM products WHERE id BETWEEN 3 and 8;

# AND: оператор и, для множества условий 

# LIKE: Выводит результат который соответсвует введенному шаблону для строк. Чувствителен к регистру
# ILIKE: тоже самое только не зависит от регистра

# ORDER BY: Сортировка по входящим данным по убываю или возрастанию.
        # ASC(по возрастанию) и DESC(по убыванию)
# Cинтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];

# Агрегационные функции  - AVG(), COUNT(), MIN(), MAX(), SUM()

# AS (ALIAS)
#  SELECT name, price * quantity AS total FROM products;

# GROUP BY разделяет данные которые мы получаем в SELECT, при этом группируя их по определнному признаку. И теперь для каждой группы можно использовать фукнцию

# SELECT city, MAX(temp_hi), AVG(prcep), SUM(temp_low) as summa_temp, MIN(date) FROM weather GROUP BY city;

# HAVING: он работает так же как и WHERE, только с оператором GROUP BY


# Команда для создания таблицы
# CREATE TABLE <tableName> (
        # <name_column> <type>,
        # <name_column> <type>,
# );
        # CREATE TABLE weather (city varchar(80),
                        #       date date,
                        #       temp int);

# DROP TABLE <name>; удаление

# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (<data>);

# INSERT INTO cities (name, location) 
# VALUES ('Bishkek', '(42, 74)'); 

# Команда обновления
# UPDATE <tablename> SET <row> = <new_value>
# WHERE <row> = <value>;

# Комнада для удаления
# DELETE FROM <tablename> WHERE <row>=<value>;

# -----------------
# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id; - Запрос сразу в две таблицы 

# JOIN соединение таблиц
# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1 JOIN orders o1 ON p1.id = o1.product_id;

# JOIN: выборка данных из двух таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: выборка будет содержать все строки из правой таблицы таблицы

# INNER JOIN: выводит все данные согласно условию


