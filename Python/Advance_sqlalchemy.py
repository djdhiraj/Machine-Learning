from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, union, union_all, except_, intersect
engine = create_engine('sqlite:///college.db', echo = True)

meta = MetaData()
conn = engine.connect()
addresses = Table(
   'addresses', meta, 
   Column('id', Integer, primary_key = True), 
   Column('st_id', Integer), 
   Column('postal_add', String), 
   Column('email_add', String)
)

u = union(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))
result = conn.execute(u)
result.fetchall()
u = union_all(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))
result = conn.execute(u)
result.fetchall()
u = except_(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.postal_add.like('%Pune')))
result = conn.execute(u)
result.fetchall()
u = intersect(addresses.select().where(addresses.c.email_add.like('%@yahoo.com')), addresses.select().where(addresses.c.postal_add.like('%Delhi')))
result = conn.execute(u)
result.fetchall()
