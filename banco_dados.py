import sqlite3
import pandas as pd
from datetime import datetime

#Criando a conexão com o banco de dados SQLite
def inicializar_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Cidade TEXT NOT NULL,
        feriado_municipal DATE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS idx_cidade_data
    ON users (Cidade, feriado_municipal)
    """)

    return conn


import os

# Caminho absoluto do banco (importante para rodar em segundo plano)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "banco_dados.db")

def conectar_banco():
    return sqlite3.connect(DB_PATH)

# Banco de dados criado e conexão estabelecida
conn = inicializar_banco()
conn.close()

print("Bem-vindo ao sistema de cadastro de feriados municipais!")



