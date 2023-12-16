use savemind;
create table if not exists savewords
(
id INT primary key auto_increment,
id_user int not null,
from_word char(2) not null,
to_word char(2) not null,
word varchar(100) not null,
translateWord varchar(100) not null,
context_word_use text,
status bit not null,
foreign key(id_user) references savemind.user_savemind(Id) on update cascade,
registration_date timestamp DEFAULT CURRENT_TIMESTAMP
)