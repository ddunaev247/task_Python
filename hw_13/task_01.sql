create table if not exists films(
    id_film serial primary key,
    name_film text,
    duration int,
    producer text,
    genre_film text not null);
)
insert into films(name_film, duration, producer, genre_film) values ('iron man', 126, 'Avi', 'fantastic,threller');
insert into films(name_film, duration, producer, genre_film) values ('cars', 121, 'Fi', 'cartoon');
insert into films(name_film, duration, producer, genre_film) values ('django', 120, 'Tarantino', 'threller');
insert into films(name_film, duration, producer, genre_film) values ('iron man 2', 110, 'Avi', 'fantastic,threller');
insert into films(name_film, duration, producer, genre_film) values ('red', 140, 'Shvenko', 'threller');
insert into films(name_film, duration, producer, genre_film) values ('argument', 135, 'Nolan', 'fantastic');

create table if not exists genres (
    id_genre serial primary key,
    genre_film text not null);


insert into genres(id_genre, genre_film) values (1, 'fantastic');
insert into genres(id_genre, genre_film) values (2, 'cartoon');
insert into genres(id_genre, genre_film) values (3, 'threller');

create table films_genre(
    id_genre integer,
    id_film integer,
    primary key (id_genre, id_film),
    constraint fk_films
        foreign key (id_film)
        references films(id_film)
        on delete cascade,
    constraint fk_ganre
        foreign key (id_genre)
        references genres (id_genre)
        on delete cascade);

insert into films_genre(id_genre, id_film) values (1, 1);
insert into films_genre(id_genre, id_film) values (1, 4);
insert into films_genre(id_genre, id_film) values (1, 6);
insert into films_genre(id_genre, id_film) values (2, 2);
insert into films_genre(id_genre, id_film) values (3, 3);
insert into films_genre(id_genre, id_film) values (3, 5);