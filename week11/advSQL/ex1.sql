create database programs;
use programs;

CREATE TABLE participants (
	participant_id INT not null auto_increment,
    first_name VARCHAR(20) not null,
    last_name VARCHAR(20) not null,
    country VARCHAR(20) not null,
    gender enum('female', 'male'),
    english_level INT,
    is_israeli BOOLEAN not null default 0,
    primary KEY(participant_id)
);

CREATE TABLE payments (
	payment_id INT not null auto_increment,
    participant_id INT,
    pay_sum INT not null,
    pay_date DATE not null,
    payment_method enum('cash', 'paypal') not null,
    authorization_code VARCHAR(10) not null unique,
    primary KEY(payment_id)
);

ALTER TABLE payments add foreign key(participant_id) references participants(participant_id) ON update cascade ON delete set null;

insert into participants
(first_name, last_name, country, gender, is_israeli_citizen)
values
("Israel", "Israeli", "Israel", 'male', true),
("Carla", "Baregel", "Italy", 'female', false);

insert into payments
(participant_id, pay_sum, pay_date, payment_method, authorization_code)
values
(1, 2000, '1999-12-01', 'cash', 'TYJDC347S'),
(2, 100, '2017-05-05', 'paypal', 'HSEC92STO');

insert into payments
(participant_id, pay_sum, pay_date, payment_method, authorization_code)
values
(5, 150, '2018-10-10', 'paypal', 'GXEDVVTM8Y');