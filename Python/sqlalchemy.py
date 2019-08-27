from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

classes = Table(
   'classes', meta, 
   Column('id', Integer, primary_key = True), 
   Column('Class_name', String), 
   Column('student_id', Integer),
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
conn.close()

ins = classes.insert()

conn = engine.connect()
conn.execute(classes.insert(), [
   {'Class_name':'10th', 'student_id' : 1},
   {'Class_name':'9th','student_id' : 2},
   {'Class_name':'12th','student_id' : 3},
   {'Class_name':'5th','student_id' : 4},
])


s = students.select()
conn = engine.connect()
result = conn.execute(s)

for row in result:
   print (row)


