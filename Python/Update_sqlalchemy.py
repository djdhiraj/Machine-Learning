from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', 
   meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

conn = engine.connect()
stmt=students.update().where(students.c.lastname=='Khanna').values(lastname='Kapoor')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()

# from sqlalchemy import create_engine
# from sqlalchemy.sql import text, alias, select
# 
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
# from sqlalchemy import and_
# from sqlalchemy.sql import select
# engine = create_engine('sqlite:///college.db', echo = True)
# meta = MetaData()
# students = Table(
#    'students', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('name', String), 
#    Column('lastname', String), 
# )
# addresses = Table(
#    'addresses', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('st_id', Integer, ForeignKey('students.id')), 
#    Column('postal_add', String), 
#    Column('email_add', String))
# 
# stmt = students.update().values({
#    students.c.name:'xyz',
#    addresses.c.email_add:'abc@xyz.com'
# }).where(students.c.id == addresses.c.id)
