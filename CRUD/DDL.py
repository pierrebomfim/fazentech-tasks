import sqlite3

conn = sqlite3.connect('fazenda.bd')
cursor = conn.cursor()

# DLL - Criação das Tabelas

cursor.execute("""
    CREATE TABLE estoque (
        id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        item            VARCHAR(10) NOT NULL,
        categoria       VARCHAR(10) NOT NULL,
        fabricante      VARCHAR(10) DEFAULT NULL,
        qtde            INTEGER     DEFAULT NULL,
        unidade         VARCHAR(2)  NOT NULL,
        movimentacao    VARCHAR(1)   NOT NULL
    );
""")
print("tabela criada com sucesso!")
conn.commit()

cursor.execute("""
    CREATE TABLE funcionarios (
        id        INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome      TEXT         NOT NULL,
        idade     INTEGER,
        sexo      VARCHAR (11) NOT NULL
        naturalidade   TEXT         NOT NULL
        cpf       VARCHAR (11) NOT NULL,
        cargo     TEXT         NOT NULL,
    );
""")
print("tabela criada com sucesso!")
conn.commit()

cursor.execute("""
    CREATE TABLE maquinario (
        id          INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
        item        VARCHAR(10) NOT NULL,
        categoria   VARCHAR(10) NOT NULL,
        fabricante  TEXT        NOT NULL,
        qtde        INTEGER     NOT NULL,
        responsavel TEXT NOT NULL,
        status      TEXT NOT NULL
    );
""")
print("tabela criada com sucesso!")
conn.commit()

cursor.close()
conn.close()

