import sqlite3
import pandas as pd
from datetime import date
 

conn = sqlite3.connect("banco_dados.db")
cursor = conn.cursor()

 #Funções para adicionar dados ao banco de dados

def adicionar_cidade():
    cidade = input("Digite o nome da cidade: ")
    feriado = input("Digite a data do feriado municipal (AAAA-MM-DD): ")

    try:
        #Verificar se a cidade já esta cadastrada
        cursor.execute("SELECT 1 FROM users WHERE Cidade = ?", (cidade,))
        resultado = cursor.fetchone()

        if resultado:
            print("Cidade já cadastrada no sistema.")
            return
        
        #Isere somante se não existir
        cursor.execute("INSERT INTO users (Cidade, feriado_municipal) VALUES (?, ?)", (cidade, feriado))
        conn.commit()
        print("Cidade e feriado municipal adicionados com sucesso!")

    except Exception as e:
        print(f"Erro ao adicionar cidade e feriado: {e}")
           

#Função para consultar feriados futuros
def consultar_feriados():
    hoje = date.today()

    #query para selecionar feriados futuros
    query = """
    SELECT Cidade, feriado_municipal
    FROM users
    WHERE feriado_municipal >= DATE('now')
    ORDER BY feriado_municipal"""

    #dataframe com os resultados
    df = pd.read_sql_query(query, conn)
        
    if df.empty:
            print("Nenhum feriado municipal encontrado a partir de hoje.")
            return
    df["feriado_municipal"] = pd.to_datetime(df["feriado_municipal"])
 
    dias_para_feriado = "Dias para o feriado"
    df[dias_para_feriado] = (df["feriado_municipal"] - pd.Timestamp(hoje)).dt.days

    print("\nFeriados futuros:")
    print(df) 
    
#Função para excluir feriado municipal de uma cidade
def excluir_feriado():
    cidade = input("Digite o nome da cidade cujo feriado deseja excluir: ")

    cursor.execute("DELETE FROM users WHERE Cidade = ?", (cidade,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Cidade excluída com sucesso!")
    else:
        print("Nenhuma cidade encontrada para exclusão.")


   


      

#MEnu de opções

while True:
    print("\n=====Menu de opções======:") 
    print("1. Adicionar cidade e feriado municipal")
    print("2. Consultar feriados municipais futuros")
    print("3. Excluir feriado municipal de uma cidade")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")
    if escolha == "1":
        adicionar_cidade()
    elif escolha == "2":
        consultar_feriados()
    elif escolha == "3":
        excluir_feriado()
    elif escolha == "4":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

#Fechando a conexão com o banco de dados
conn.close()