import sqlite3
import pandas as pd
from datetime import date
from plyer import notification

#Criando a conexão com o banco de dados SQLite
conn = sqlite3.connect("banco_dados.db")

#Le os dados do banco de dados
df = pd.read_sql_query("SELECT Cidade, feriado_municipal FROM users", conn)

conn.close()
#Obtém a data atual
hoje = date.today()

#converte para data
df["feriado_municipal"] = pd.to_datetime(df["feriado_municipal"], format="mixed")

#Dias restantes para o feriado
df["Dias para o feriado"] = (df["feriado_municipal"] - pd.Timestamp(hoje)).dt.days

#Filtra os feriados 3 dias antes do vencimento
avisos = df[df["Dias para o feriado"] == 3]

#Envia notificações para cada feriado encontrado

for _, linha in avisos.iterrows():
    notification.notify(
        title = "Alerta de Feriado Municipal",
        message = f"Em 3 dias será feriado em {linha['Cidade']} no dia {linha['feriado_municipal'].date()}!",
        timeout = 10
    )


print("Notificações de feriados municipais enviadas (se houver feriados em 3 dias).")



    
  
