# Bibliotecas utilizadas
from validacao import Validacao
from Questao_4.analisar_entrada import AnalisarEntrada

import os
import sys


# Variável que guardará as opções do menu
opcoes_do_menu = """
[ 1 ] = Adicionar uma nova entrada
[ 2 ] = Voltar para o menu anterior
[ 3 ] = Sair do programa
"""

# Criando objeto da classe para efetuar os seus métodos
analisar = AnalisarEntrada()


# Classe Menu
class MenuQuestao4:

    #  Método estático para a criação do menu principal da questão 3
    @staticmethod
    def menu_principal_questao_4():

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
                print(f"\n{analisar.analisar_mensagem(entrada)}")
            
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
