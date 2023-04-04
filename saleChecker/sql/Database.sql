-- In here I'll comment on the implementation of a database for the collection of the games in which I am interested
-- obviously, this being in a Database is not really useful for me but learning about it's implementation could be cool

create database steamgames;
\c steamgames

create table juegos(
  name VARCHAR(100) PRIMARY KEY,
  onsale VARCHAR(5) NOT NULL,
  currency VARCHAR(10) NOT NULL,
  price NUMERIC NOT NULL,
  url VARCHAR(200) NOT NULL
);

