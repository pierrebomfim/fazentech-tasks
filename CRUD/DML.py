import sqlite3

conn = sqlite3.connect('fazenda.bd')
cursor = conn.cursor()

# DML - Inserção de dados

cursor.execute("""
    INSERT INTO estoque (item, categoria, fabricante, qtde, unidade, movimentacao)
    VALUES  ('diesel', 'combustivel', 'shell', 100, 'l', 'e'),
            ('ureia', 'fertilizantes','',100, 'kg', 'e'),
            ('pneu', 'auto','pirelli', 5, 'un', 'e'), 
            ('glifosato', 'herbicidas','',50, 'l', 'e'),
            ('diesel', 'combustivel', 'petrox', 10, 'l', 's')
""")
print("DB atualizado com sucesso!")

# Ao contrário de idade, será inserido a data de nascimento na tabela. Segue codigo para atualizar a coluna:

cursor.execute("""
    ALTER TABLE funcionarios RENAME COLUMN idade TO nascimento
""")
print("coluna renomeada com sucesso!")

cursor.execute("""
    INSERT INTO funcionarios ( nome, nascimento, sexo, naturalidade, cpf, cargo)
    VALUES  ('Antônio Carlos', '0000-00-00', 'M', 'Brasil', 02993499000, 'operador'),
            ('José de Almeida', '1976-06-13','M', 'Brasil', 01124354387, 'supervisor'),
            ('Maria Lúcia', '1986-06-11','F', 'Brasil', 02902902976, 'operador'),
            ('André dos Santos', '1989-09-13', 'M', 'Brasil', 34523443245, 'operador'),
            ('Paula de Oliveira', '1966-03-19', 'F', 'Brasil', 45454534326, 'zeladora')
""")
print("DB atualizado com sucesso!")

cursor.execute("""
    INSERT INTO maquinario ( item, categoria, fabricante, qtde, responsavel, status)
    VALUES  ('misturador','agrícola', '', 5, 1, 'funcionando'),
            ('misturador','agrícola', '', 1, 1, 'sucata'),
            ('trator','agrícola','caterpillar', 2, 3,'funcionando'),
            ('carreta','transporte', '', 1, 3, 'funcionando'),
            ('empillhadeira','transporte', 'caterpillar', 2, 4,'funcionando')
""")
print("DB atualizado com sucesso!")

conn.commit()
cursor.close()
conn.close()