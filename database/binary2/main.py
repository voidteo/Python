import psycopg2 


conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "test_db",
    user = "postgres",
    password = "teopostgres"
)

cur = conn.cursor()

stmt = """
create table if not exists students(
    id serial primary key,
    first_name varchar(50),
    last_name varchar(50),
    grade varchar(10),
    age int
)
"""

cur.execute(stmt)
conn.commit()

stmt = """
insert into students(first_name, last_name, grade, age)
values('eshmat', 'teshayev', 'C', 20)
"""

cur.execute(stmt)
conn.commit()

cur.execute("select * from students")

row = cur.fetchall()
print(row)

conn.close()

