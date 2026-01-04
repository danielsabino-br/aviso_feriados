import time
import os
from datetime import datetime
from funcoes import verificar_feriados_em_5_dias

# Diretório base do projeto (importante para execução em segundo plano)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_EXECUCAO = os.path.join(BASE_DIR, "log_execucao.txt")
LOG_ERRO = os.path.join(BASE_DIR, "log_erro.txt")

# Aguarda o Windows inicializar completamente
time.sleep(30)

while True:
    try:
        verificar_feriados_em_5_dias()

        with open(LOG_EXECUCAO, "a", encoding="utf-8") as f:
            f.write(f"[OK] Execução realizada em {datetime.now()}\n")

    except Exception as e:
        with open(LOG_ERRO, "a", encoding="utf-8") as f:
            f.write(f"[ERRO] {datetime.now()} - {repr(e)}\n")

    # Aguarda 1 hora
    time.sleep(60 * 60)

