# Scrip para iserção de dados nas tabelas

import sqlite3

conn = sqlite3.connect('fazenda.bd')
cursor = conn.cursor()

# Tabela estoque
print('Tabela Estoque')
item = input('Digite o item: ')
categoria = input('Digite a categoria: ')
fabricante = input('Digite o fabricante: ')
qtde = int(input('Digite a quantidade: '))
unidade = input('Digite a unidade de medida: ')
movimentacao = input('Digite E para material entrando e S para saída: ')

sql = f"INSERT INTO estoque (item, categoria, fabricante, qtde, unidade, movimentacao) VALUES ('{item}', '{categoria}', '{fabricante}', '{qtde}', '{unidade}', '{movimentacao}')"

cursor.execute(sql)

# Tabela funcionarios
print('Tabela Funcionários')
item = input('Digite o nome do funcionário: ')
nascimento = input('Digite a data de nascimento aaaa-mm-dd: ')
sexo = input('Digite o sexo M/F: ')
naturalidade = input('Digite a naturalidade: ')
cpf = input('Digite o CPF: ')
cargo = input('Digite o cargo: ')

sql = f"INSERT INTO funcionarios ( nome, nascimento, sexo, naturalidade, cpf, cargo) VALUES ('{item}', '{nascimento}', '{sexo}', '{naturalidade}', '{cpf}', '{cargo}')"

cursor.execute(sql)

# Tabela maquinario
print('Tabela Maquinário')
item = input('Digite o item: ')
categoria = input('Digite a categoria: ')
fabricante = input('Digite o fabricante: ')
qtde = int(input('Digite a quantidade: '))
responsavel = input('Digite o ID do responsável: ')
status = input('Digite o status: ')

sql = f"INSERT INTO maquinario ( item, categoria, fabricante, qtde, responsavel, status) VALUES ('{item}', '{categoria}', '{fabricante}', '{qtde}', '{responsavel}', '{status}')"

cursor.execute(sql)


conn.commit()
cursor.close()
conn.close()