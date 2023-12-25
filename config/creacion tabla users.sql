use savemind;
create table if not exists User_saveMind
(
	Id int auto_increment primary key,
	name varchar(45) not null,
    lastname varchar(50) not null,
    number BIGINT(15) not null,
    email varchar(25) unique not null,
    password varchar(64) not null,
    birthday date not null,
    registration_date timestamp DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE savemind.user_savemind MODIFY COLUMN number BIGINT;