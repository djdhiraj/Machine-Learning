from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)
meta.create_all(engine)
ins = students.insert()

conn = engine.connect()
conn.execute(students.insert(), [
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])

s = students.select()
conn = engine.connect()
result = conn.execute(s)

for row in result:
   print (row)


