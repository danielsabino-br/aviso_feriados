import pandas as pd
from datetime import date, datetime, timedelta
from banco_dados import conectar_banco
from notification import notificar


def adicionar_cidade():
    conn = conectar_banco()
    cursor = conn.cursor()

    cidade = input("Digite o nome da cidade: ")
    feriado = input("Digite a data do feriado municipal (AAAA-MM-DD): ")

    try:
        cursor.execute("SELECT 1 FROM users WHERE Cidade = ?", (cidade,))
        if cursor.fetchone():
            print("Cidade já cadastrada no sistema.")
            return

        cursor.execute(
            "INSERT INTO users (Cidade, feriado_municipal) VALUES (?, ?)",
            (cidade, feriado)
        )
        conn.commit()
        print("Cidade e feriado municipal adicionados com sucesso!")

    except Exception as e:
        print(f"Erro ao adicionar cidade e feriado: {e}")

    finally:
        conn.close()


def consultar_feriados():
    conn = conectar_banco()

    hoje = date.today()

    query = """
        SELECT Cidade, feriado_municipal
        FROM users
        WHERE feriado_municipal >= DATE('now')
        ORDER BY feriado_municipal
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    if df.empty:
        print("Nenhum feriado municipal encontrado a partir de hoje.")
        return

    df["feriado_municipal"] = pd.to_datetime(df["feriado_municipal"])
    df["Dias para o feriado"] = (df["feriado_municipal"] - pd.Timestamp(hoje)).dt.days

    print("\nFeriados futuros:")
    print(df)


def excluir_feriado():
    conn = conectar_banco()
    cursor = conn.cursor()

    cidade = input("Digite o nome da cidade cujo feriado deseja excluir: ")

    cursor.execute("DELETE FROM users WHERE Cidade = ?", (cidade,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Cidade excluída com sucesso!")
    else:
        print("Nenhuma cidade encontrada para exclusão.")

    conn.close()


def verificar_feriados_em_5_dias():
    conn = conectar_banco()
    cursor = conn.cursor()

    hoje = datetime.now().date()
    data_alvo = hoje + timedelta(days=5)

    cursor.execute("""
        SELECT Cidade, feriado_municipal
        FROM users
        WHERE feriado_municipal = ?
    """, (data_alvo.strftime("%Y-%m-%d"),))

    resultados = cursor.fetchall()
    conn.close()

    for cidade, data in resultados:
        notificar(
            f"📅 Atenção: Faltam 5 dias para o feriado municipal em {cidade} ({data})"
        )



