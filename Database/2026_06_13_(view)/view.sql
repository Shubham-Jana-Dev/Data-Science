use my_practice;
show TABLEs;
create table cars(model varchar(100), price bigint, brand varchar(100), car_id int);
insert into cars values('az7', 2044330, 'suzuki', 12), ('qw3', 239902, 'mahindrea', 14),('pwr',322432, 'Hindusthan motor', 78);
select * from cars;
insert into cars values('wr4', 456633340, 'KIA', 18), ('yt54', 456684443, 'GM', 194),('p1r',32243234, 'Tata', 32);

create view expencive_car as select model,price from cars where price > 34222556674;
select* from expencive_car;