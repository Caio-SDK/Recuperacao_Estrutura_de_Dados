# Bibliotecas utilizadas
from validacao import Validacao
from Questao_1.analisar_string import AnalisarString

import os
import sys


# Variável que guardará as opções do menu
opcoes_do_menu = """
[ 1 ] = Analisar uma nova entrada
[ 2 ] = Voltar para o menu anterior
[ 3 ] = Sair do programa
"""

# Criando objeto da classe para efetuar os seus métodos
analisar = AnalisarString()


# Classe Menu
class MenuQuestao1:

    #  Método estático para a criação do menu principal da questão 1
    @staticmethod
    def menu_principal_questao_1():

        while True:

            # Exibição das opções
            print(opcoes_do_menu)

            # Requisitando uma opção desejada ao usuário
            opcao = Validacao.ValidacaoNumeroInteiro("Digite sua opção: ")

            # Limpando o terminal para não haver poluição visual
            os.system("cls")

            # Opção 1
            if opcao == 1:

                # Requisitando uma entrada para o algoritmo anaisar
                entrada = input("Digite a entrada a ser analisada: ")

                # Exibição da saída
                print(f"\n{analisar.analisar_string(entrada)}")
            
            # Opção 2
            elif opcao == 2:

                # Fim do laço de repetição para voltar ao menu anterior
                break
            
            # Opção 3
            elif opcao == 3:

                # Saindo do programa
                sys.exit()
            
            # Opção inválida
            else:

                print("\nDigite uma opção válida!!!\n")