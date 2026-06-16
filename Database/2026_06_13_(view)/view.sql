use my_practice;
show TABLEs;
create table cars(model varchar(100), price bigint, brand varchar(100), car_id int);
insert into cars values('az7', 2044330, 'suzuki', 12), ('qw3', 239902, 'mahindrea', 14),('pwr',322432, 'Hindusthan motor', 78);
select * from cars;
insert into cars values('wr4', 456633340, 'KIA', 18), ('yt54', 456684443, 'GM', 194),('p1r',32243234, 'Tata', 32);
-- problem 1.

create view avarage_car as select model,price from cars where price < 556674;
select* from avarage_car;

create Table student1(s_id int AUTO_INCREMENT PRIMARY KEY,
s_name VARCHAR(100),
s_phon BIGINT,
s_address TEXT);

insert into student1 VALUES(37,'Suresh',98003234,'suresh@gmail.com'),(Null,'Dipak',999909253,'dip@ee33');
insert into student1 VALUES(44, 'Bikash',98778678,'bikash23@outlook.com');
select*from student1;

create Table s_parents(p_id INT AUTO_INCREMENT PRIMARY KEY,
p_name VARCHAR(100));

insert into s_parents VALUES(35, 'H'),(36, 'M'),(37, 'P'),(38, 'D');
insert into s_parents VALUES(39,'P');
update s_parents set p_name = 'J' where p_id = 37;
select* FROM s_parents;
select * from student1 right OUTER JOIN s_parents on student1.s_id = s_parents.p_id;

select s_id,s_name,p_id,p_name from student1 right OUTER JOIN s_parents on student1.s_id = s_parents.p_id GROUP BY s_id, p_id;
create View student_parents as select s_id,s_name,p_id,p_name from student1 right OUTER JOIN s_parents on student1.s_id = s_parents.p_id GROUP BY s_id, p_id;

select * from student_parents;