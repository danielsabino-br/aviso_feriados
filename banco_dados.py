import sqlite3
import pandas as pd
from datetime import datetime

#Criando a conexão com o banco de dados SQLite
conn = sqlite3.connect('banco_dados.db')
cursor = conn.cursor()

#Criando a tabela de transações se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Cidade TEXT NOT NULL,
    feriado_municipal DATE NOT NULL
)       
''')

cursor.execute('''
CREATE UNIQUE INDEX IF NOT EXISTS idx_cidade ON users (Cidade)
''')

conn.commit()

print("Bem-vindo ao sistema de cadastro de feriados municipais!")



