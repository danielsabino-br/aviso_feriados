import sqlite3
import time
from datetime import datetime

def verificar_feriado():
    conn = sqlite3.connect('banco_dados.db')
    cursor = conn.cursor()

    hoje = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT Cidade FROM users
        WHERE feriado_municipal = ?
    """, (hoje,))

    cidades = cursor.fetchall()
    conn.close()

    if cidades:
        for cidade in cidades:
            print(f"🎉 Hoje é feriado municipal em {cidade[0]}!")
    else:
        print("Hoje não há feriados municipais cadastrados.")

# 🔁 Loop em segundo plano
while True:
    verificar_feriado()
    time.sleep(60 * 60)  # verifica a cada 1 hora
