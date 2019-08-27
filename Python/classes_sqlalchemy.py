from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import and_
from sqlalchemy.sql import select
engine = create_engine('sqlite:///college.db', echo = True)
conn = engine.connect()
s = select([text("* from students")]) \
.where(
   and_(
      text("students.name between :x and :y"),
      text("students.id>2")
   )
)
conn.execute(s, x = 'A', y = 'L').fetchall()
