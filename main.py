# Bibliotecas utilizadas
from Questao_3.menu_questao_3 import MenuQuestao3
from Questao_4.menu_questao_4 import MenuQuestao4

import os
import sys


mensagem = """
[ 1 ] = Visualizar questão 1
[ 2 ] = Visualizar questão 2
[ 3 ] = Visualizar questão 3
[ 4 ] = Visualizar questão 4
[ 5 ] = Sair do programa
"""

while True:

    print(mensagem)

    opc = int(input("Digite sua opção: "))

    os.system("cls")

    if opc == 1:

        pass

    elif opc == 2:

        pass

    elif opc == 3:

        MenuQuestao3.menu_principal_questao_3()
    
    elif opc == 4:

        MenuQuestao4.menu_principal_questao_4()

    elif opc == 5:

        print("\n\nObrigado por teste!!!\n")
        sys.exit()

    else:

        print("Digite uma opção válidação!!!")