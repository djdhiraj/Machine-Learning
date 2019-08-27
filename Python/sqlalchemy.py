
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
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
addresses = Table(
   'addresses', meta, 
   Column('id', Integer, primary_key = True), 
   Column('st_id', Integer, ForeignKey('students.id')), 
   Column('postal_add', String), 
   Column('email_add', String))


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

conn.execute(addresses.insert(), [
   {'st_id':1, 'postal_add':'Shivajinagar Pune', 'email_add':'ravi@gmail.com'},
   {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
   {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
   {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
   {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
])
s = students.select()
conn = engine.connect()
result = conn.execute(s)

for row in result:
   print (row)


