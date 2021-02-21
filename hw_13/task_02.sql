create table if not exists songs(
    id_song serial primary key,
    name_song text,
    duration int,
    singer text
    );
)
insert into songs(name_song, duration, singer) values ('track_1',2, 'Avi');
insert into songs(name_song, duration, singer) values ('Red',3, 'Avi,Joni');
insert into songs(name_song, duration, singer) values ('Yellow',4, 'Joni');
insert into songs(name_song, duration, singer) values ('track_2',2, 'Avi');
insert into songs(name_song, duration, singer) values ('track',2, 'Lucy');
insert into songs(name_song, duration, singer) values ('Moskow',5, 'Richi,Lucy');

create table if not exists singers(
    id_singer serial primary key,
    name_singer text not null);

insert into singers(name_singer) values ('Avi');
insert into singers(name_singer) values ('Joni');
insert into singers(name_singer) values ('Lucy');
insert into singers(name_singer) values ('Richi');

create table if not exists tracks(
    id_singer integer,
    id_song integer,
    primary key (id_singer, id_song),
    constraint fk_song
        foreign key (id_song)
        references songs(id_song)
        on delete cascade,
    constraint fk_singer
        foreign key (id_singer)
        references singers (id_singer)
        on delete cascade);
)
insert into tracks(id_singer,id_song) values (1,1)
insert into tracks(id_singer,id_song) values (1,2)
insert into tracks(id_singer,id_song) values (1,4)
insert into tracks(id_singer,id_song) values (2,2)
insert into tracks(id_singer,id_song) values (2,3)
insert into tracks(id_singer,id_song) values (3,5)
insert into tracks(id_singer,id_song) values (3,6)
insert into tracks(id_singer,id_song) values (4,6)