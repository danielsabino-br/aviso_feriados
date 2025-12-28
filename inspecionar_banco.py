import sqlite3
import pandas as pd

# Conecta ao banco
conn = sqlite3.connect("banco_dados.db")

# Lista todas as tabelas do banco
tabelas = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("📌 Tabelas existentes no banco:")
print(tabelas)

# Para cada tabela, mostrar todos os dados
for tabela in tabelas["name"]:
    print(f"\n📄 Conteúdo da tabela: {tabela}")
    df = pd.read_sql_query(f"SELECT * FROM {tabela}", conn)
    print(df)

# Fecha a conexão
conn.close()


