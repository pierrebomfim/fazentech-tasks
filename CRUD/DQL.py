import sqlite3

conn = sqlite3.connect('fazenda.bd')
cursor = conn.cursor()


# Consulta do número total de funcionários

sql = "SELECT COUNT(id) FROM funcionarios"
cursor.execute(sql)
dados = cursor.fetchall()
for d in dados:
  print(f'O número total de funcionários é {d}')


# Consulta do número de funcionários homens e mulheres

sql = "SELECT sexo, COUNT(id) FROM funcionarios GROUP BY sexo"
cursor.execute(sql)
dados = cursor.fetchall()
for d in dados:
  print(d)


# Consulta qual funcionário é responsável por cada maquinário

cursor.execute("""
    
  SELECT funcionarios.id, funcionarios.nome, maquinario.item FROM funcionarios INNER JOIN maquinario
  ON maquinario.responsavel = funcionarios.id ORDER BY funcionarios.nome

""")
dados = cursor.fetchall()
for d in dados:
  print(d)


cursor.close()
conn.close()