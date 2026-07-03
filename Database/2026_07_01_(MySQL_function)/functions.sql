use my_practice;
create table my_student(s_id int, marks int);
alter table My_student add department varchar(100);
insert into my_student(s_id, marks, department) VALUES(44,233, "CSE"),(2,334, "ECE"),(3,443, "EEE"),(4,123, "DBMS");
delimiter @
create function f4221( w varchar(100)) returns varchar(100)
DETERMINISTIC NO SQL reads sql data
begin
declare w varchar(100);
declare a varchar(100);
select s_id into a from my_student where department = w;
return a;
end @
select f4221("EEE");
select * from my_student;