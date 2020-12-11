import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('fazenda.bd')
cursor = conn.cursor()

df = pd.read_sql_query('select * from funcionarios', conn)

# À fazer: realizar vários tipos de busca possiveis aqui

# Busca Binária com o ID do funcionário
funcionario = df['id'].to_numpy()
nome = df['nome'].to_numpy()

def buscar_funcionario(funcionario, id):
  min, max = 0, len(funcionario) -1 
  while min <= max:
    mid = int(min + max) // 2
    if id < funcionario[mid]:
      max = mid - 1
    elif id > funcionario[mid]:
      min = mid + 1
    else:
      return mid
  return None

id = int(input(f'Digite o id: '))
result = buscar_funcionario(funcionario, id)
if result:
  print(f'\nO funcionário {nome[result]} foi encontrado no index {result}.')
else:
  print('\nFuncionário não cadastrado!')
## Verificar erro ao fazer busca com o id 1