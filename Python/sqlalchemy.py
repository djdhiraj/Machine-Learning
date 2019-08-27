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

SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (select * from Students);
select * from Students LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT type,name,sql,tbl_name,'0' AS temp FROM sqlite_master UNION SELECT type,name,sql,tbl_name,'1' AS temp FROM sqlite_temp_master;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (select * from Students);
select * from Students LIMIT 0, 50000;
SELECT type,name,sql,tbl_name,'0' AS temp FROM sqlite_master UNION SELECT type,name,sql,tbl_name,'1' AS temp FROM sqlite_temp_master;
SELECT COUNT(*) FROM (select * from Students);
select * from Students LIMIT 0, 50000;
SELECT COUNT(*) FROM (select * from Students);
select * from Students LIMIT 0, 50000;

SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT type,name,sql,tbl_name,'0' AS temp FROM sqlite_master UNION SELECT type,name,sql,tbl_name,'1' AS temp FROM sqlite_temp_master;


SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `students` WHERE `id` LIKE '%1%' ESCAPE '\' AND `name` LIKE '%dhiraj%' ESCAPE '\' AND `lastname` LIKE '%kumar%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (select * from 'class');
select * from 'class' LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT COUNT(*) FROM (select * from 'class'));
SELECT COUNT(*) FROM (select * from 'class') LIMIT 0, 50000;
