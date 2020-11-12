CREATE DATABASE fazenda;

USE fazenda;

CREATE TABLE funcionarios (
id int Not Null auto_increment,
nome varchar(30) not null,
nascimento date,
sexo enum('M', 'F'),
nacionalidade varchar(10) default 'Brasil',
cpf int(11),
funcao varchar(10),
primary key (id)
) default charset = utf8;

describe funcionarios;

CREATE TABLE estoque (
id int Not Null auto_increment,
item varchar(10) not null,
categoria varchar(10) not null,
fabricante decimal(4,1),
qtde int(3),
unidade enum('L', 'Kg', 'Pc'),
movimentacao enum('E', 'S'),
primary key (id)
) default charset = utf8;

describe estoque;