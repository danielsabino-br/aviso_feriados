import sqlite3
import pandas as pd
from datetime import date
from plyer import notification

#Criando a conexão com o banco de dados SQLite
conn = sqlite3.connect("banco_dados.db")

df = pd.read_sql_query(
    "SELECT Cidade, feriado_municipal FROM users",
    conn
)

conn.close()

hoje = date.today()

df["feriado_municipal"] = pd.to_datetime(df["feriado_municipal"])

df["Dias para o feriado"] = (
    df["feriado_municipal"] - pd.Timestamp(hoje)
).dt.days

avisos = df[(df["Dias para o feriado"] > 0) & (df["Dias para o feriado"] <= 3)]

for _, linha in avisos.iterrows():
    notification.notify(
        title="Alerta de Feriado Municipal",
        message=(
            f"Faltam {linha['Dias para o feriado']} dias "
            f"para o feriado em {linha['Cidade']} "
            f"({linha['feriado_municipal'].date()})"
        ),
        timeout=10
    )
print("Notificações de feriados municipais enviadas (se houver).")







    
  
