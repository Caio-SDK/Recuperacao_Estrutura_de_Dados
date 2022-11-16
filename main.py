# Bibliotecas utilizadas
from Questao_1.menu_questao_1 import MenuQuestao1
from Questao_2.menu_questao_2 import MenuQuestao2
from Questao_3.menu_questao_3 import MenuQuestao3
from Questao_4.menu_questao_4 import MenuQuestao4

# Biblioteca de validação
from validacao import Validacao

# Bibliotecas de sistema
import os
import sys


# Opções do menu interativo
mensagem = """
[ 1 ] = Visualizar questão 1
[ 2 ] = Visualizar questão 2
[ 3 ] = Visualizar questão 3
[ 4 ] = Visualizar questão 4
[ 5 ] = Sair do programa
"""

while True:

    # Exibição das opções
    print(mensagem)

    # Requisitando uma opção para o usuário
    opcao_desejada = Validacao.ValidacaoNumeroInteiro("Digite sua opção: ")

    # Limpando o terminal para não haver poluição visual
    os.system("cls")

    # Opção 1
    if opcao_desejada == 1:

        MenuQuestao1.menu_principal_questao_1()

    # Opção 2
    elif opcao_desejada == 2:

        MenuQuestao2.menu_principal_questao_2()

    # Opção 3
    elif opcao_desejada == 3:

        MenuQuestao3.menu_principal_questao_3()
    
    # Opção 4
    elif opcao_desejada == 4:

        MenuQuestao4.menu_principal_questao_4()

    # Opção 5
    elif opcao_desejada == 5:

        print("\n\nObrigado por teste!!!\n")
        sys.exit()

    # Opção inválida
    else:

        print("Digite uma opção válidação!!!")