-- Criando a DB
create database noticias;

-- Acessando a DB
use noticias;

-- url,titulo,publicacao,texto,tags

-- Criando as tabelas e definindo a URL como UNIQUE para não haver replicas de noticias.
create table if not exists bbc (
url varchar (500),
titulo text,
publicacao datetime,
texto text,
tags text,
UNIQUE (url)
);

create table if not exists cnn (
url varchar (500),
titulo text,
publicacao datetime,
texto text,
tags text,
UNIQUE (url)
);

create table if not exists metropoles (
url varchar (500),
titulo text,
publicacao datetime,
texto text,
tags text,
UNIQUE (url)
);
 
create table if not exists uol (
url varchar (500),
titulo text,
publicacao datetime,
texto text,
UNIQUE (url)
);


-- show tables;
-- select * from bbc;
-- select * from uol;
-- select * from cnn;
-- select * from metropoles;
