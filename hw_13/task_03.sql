create table if not exists cars(
    id_car serial primary key,
    name_car text,
    manufacturer text,
    color text,
    price int
    );
)

create table if not exists manufacturers(
    id_manufacturer   int primary key,
    name_manufacturer text,
    rating            real,
    foreign key (id_manufacturer)
    references cars(id_car)
    );

create table if not exists colors(
    id_color int primary key,
    name_color text);
)
insert into cars(name_car, manufacturer, color, price) values ('model S', 'Tesla','Red, White, Black', 44000)
insert into cars(name_car, manufacturer, color, price) values ('model Y', 'Tesla','Red, White', 48000)
insert into cars(name_car, manufacturer, color, price) values ('Audi A8', 'WVGroup','Red, White, Blue', 35000)
insert into cars(name_car, manufacturer, color, price) values ('Audi A6', 'WVGroup','Red, White, Blue', 30000)
insert into cars(name_car, manufacturer, color, price) values ('Fiat Punto', 'FiatGroup','Red, Blue', 10000)
insert into cars(name_car, manufacturer, color, price) values ('Fiat Stilo', 'FiatGroup','Red, Black', 11000)

insert into manufacturers(id_manufacturer, name_manufacturer, rating) values (1,'Tesla', 9)
insert into manufacturers(id_manufacturer, name_manufacturer, rating) values (2,'WVGroup', 8.5)
insert into manufacturers(id_manufacturer, name_manufacturer, rating) values (3,'FiatGroup', 6.5)

insert into colors(id_color, name_color) values (1, 'Red')
insert into colors(id_color, name_color) values (2, 'White')
insert into colors(id_color, name_color) values (3, 'Black')
insert into colors(id_color, name_color) values (4, 'Blue')

create table if not exists colors_cars(
    id_color int,
    id_car int,
    primary key (id_color, id_car),
    constraint fk_car
        foreign key (id_car)
        references cars(id_car)
        on delete cascade,
    constraint fk_color
        foreign key (id_color)
        references colors (id_color)
        on delete cascade);
)
insert into colors_cars(id_color, id_car) values (1,1)
insert into colors_cars(id_color, id_car) values (1,2)
insert into colors_cars(id_color, id_car) values (1,3)
insert into colors_cars(id_color, id_car) values (1,4)
insert into colors_cars(id_color, id_car) values (1,5)
insert into colors_cars(id_color, id_car) values (1,6)
insert into colors_cars(id_color, id_car) values (2,1)
insert into colors_cars(id_color, id_car) values (2,2)
insert into colors_cars(id_color, id_car) values (2,3)
insert into colors_cars(id_color, id_car) values (2,4)
insert into colors_cars(id_color, id_car) values (3,1)
insert into colors_cars(id_color, id_car) values (3,6)
insert into colors_cars(id_color, id_car) values (4,3)
insert into colors_cars(id_color, id_car) values (4,4)