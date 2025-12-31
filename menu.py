from funcoes import (
    adicionar_cidade,
    consultar_feriados,
    excluir_feriado
)

while True:
    print("\n===== Menu de opções =====")
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
        print("Opção inválida.")
        print("Por favor, escolha uma opção válida (1-4).")

