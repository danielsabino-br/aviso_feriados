#INSERINDO DADOS 

import sqlite3

conn = sqlite3.connect("banco_dados.db")
cursor = conn.cursor()  

dados = [
    ("Bauru", "2026-08-01"),
    ("Marilia", "2026-04-04"),
    ("Pompeia", "2026-09-17"),
    ("Lins", "2026-04-21"),
    ("Araçatuba", "2026-12-02"),
    ("Presidente Prudente", "2026-09-14"),
    ("Ourinhos", "2026-12-13"),
    ("Assis", "2026-05-01"),
    ("Jaú", "2026-08-15"),
    ("Botucatu", "2026-04-14"),
    ("São Jose do Rio Preto", "2026-03-14"),
]

cursor.executemany("INSERT INTO users (Cidade, feriado_municipal) VALUES (?, ?)", dados)
conn.commit()
conn.close()

print("Dados inseridos com sucesso no banco de dados.")
    