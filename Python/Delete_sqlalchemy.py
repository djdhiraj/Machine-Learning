from sqlalchemy.sql.expression import update
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)

meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

conn = engine.connect()
stmt = students.delete().where(students.c.lastname == 'Khanna')
# stmt = users.delete().where(users.c.id == addresses.c.id).where(addresses.c.email_address.startswith('xyz%'))
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()
