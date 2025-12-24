import time
from datetime import datetime, timedelta
from banco_dados import conectar_banco
from notification import notificar

def verificar_feriados_em_3_dias():
    conn = conectar_banco()   
    cursor = conn.cursor()

    hoje = datetime.now().date()
    data_alvo = hoje + timedelta(days=3)

    cursor.execute("""
        SELECT Cidade, feriado_municipal
        FROM users
        WHERE feriado_municipal = ?
    """, (data_alvo.strftime("%Y-%m-%d"),))

    resultados = cursor.fetchall()
    conn.close()

    if resultados:
        for cidade, data in resultados:
            notificar(
                f"📅 Atenção: Faltam 3 dias para o feriado municipal em {cidade} ({data})"
            )
    else:
        print("Nenhum feriado municipal em 3 dias.")

# 🔁 Rodando em segundo plano
while True:
    verificar_feriados_em_3_dias()
    time.sleep(60 * 60 * 6)  # verifica a cada 6 horas
