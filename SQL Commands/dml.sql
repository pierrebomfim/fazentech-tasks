USE fazenda;

INSERT INTO funcionarios ( id, nome, nascimento, sexo, nacionalidade, cpf, funcao) VALUES 
( default, 'Antônio Carlos', '1988-02-30', 'M', default, '02993499000', 'operador'),
( default, 'José de Almeida', '1976-06-13', 'M', default, '01124354387', 'supervisor'),
( default, 'Maria Lúcia', '1986-06-11', 'F', default, '34354565632', 'operador'),
( default, 'André dos Santos', '1989-09-13', 'M', default, '34523443245', 'operador'),
( default, 'Paula de Oliveira', '1966-03-19', 'F', default, '45454534326', 'zeladora');

SELECT * FROM funcionarios;

UPDATE funcionarios
set cpf = '02902902976'
where nome = 'Maria Lúcia';

ALTER TABLE funcionarios
modify column cpf varchar(11);

INSERT INTO estoque ( id, item, categoria, fabricante, qtde, unidade, movimentacao) VALUES 
( default, 'diesel', 'combustível', 's10' , 100, 'L', 'E'),
( default, 'ureia', 'fertilizantes', '', 100, 'Kg', 'E'),
( default, 'pneu', 'combustível', 'pirelli' , 5, 'Pc', 'E'),
( default, 'glifosato', 'herbicidas', '', 50, 'L', 'E'),
( default, 'diesel', 'combustível', 's10', 10, 'L', 'S');

SELECT * FROM estoque;
describe estoque;

ALTER TABLE estoque
modify column fabricante varchar(10);

truncate estoque;

INSERT INTO maquinario ( id, item, categoria, fabricante, qtde, responsavel, funcionando) VALUES 
( default, 'misturador', 'agrícola', '' , 2, 1, 'S'),
( default, 'misturador', 'agrícola', '', 1, 1, 'N'),
( default, 'trator', 'agrícola', 'Jonh Deere' , 1, 3, 'S'),
( default, 'carreta', 'transporte', 'bandeirante', 1, 4, 'S'),
( default, 'empillhadeira', 'transporte', 'Hyster', 1, 4, 'S');

SELECT * FROM maquinario;