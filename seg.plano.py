import time
from datetime import datetime
from funcoes import verificar_feriados_em_5_dias

time.sleep(30)  # aguarda o Windows iniciar tudo

while True:
    try:
        verificar_feriados_em_5_dias()

        with open("log_execucao.txt", "a", encoding="utf-8") as f:
            f.write(f"Execução em {datetime.now()}\n")

    except Exception as e:
        with open("log_erro.txt", "a", encoding="utf-8") as f:
            f.write(f"Erro em {datetime.now()}: {e}\n")

    time.sleep(60 * 60 * 1)  # 1 hora
