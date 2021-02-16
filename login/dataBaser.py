import sqlite3 # importar sqlite para gerar banco de dados

conn = sqlite3.connect('UserData.db') # Nome de variavel padrao para gerar a conexão com o banco de dados. O nome do arquivo o Python cria sozinho.

cursor = conn.cursor() # criando o cursor

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""") # criando colunas da tabela O Primary Key define que ele será a chave principal, Autoincrement ele gera automaticamente

print('Conectado ao banco de dados.') # printa para mostrar que deu certo a conexao.

