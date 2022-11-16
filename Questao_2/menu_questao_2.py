# Bibliotecas utilizadas
from validacao import Validacao
from Questao_2.back_space import BackSpace

import os
import sys


# Variável que guardará as opções do menu
opcoes_do_menu = """
[ 1 ] = Analisar duas entradas
[ 2 ] = Voltar para o menu anterior
[ 3 ] = Sair do programa
"""

# Criando objeto da classe para efetuar os seus métodos
back_space = BackSpace()


# Classe Menu
class MenuQuestao2:

    #  Método estático para a criação do menu principal da questão 2
    @staticmethod
    def menu_principal_questao_2():

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
                primeira_entrada = input("Digite a entrada a ser analisada: ")
                segunda_entrada = input("Digite a entrada a ser analisada: ")

                # Decodificar as mensagens recebidas como entrada
                mensagem_primaria = back_space.decodificar_mensagem(primeira_entrada)
                mensagem_secundaria = back_space.decodificar_mensagem(segunda_entrada)

                # Se as duas mensagens forem iguais
                if mensagem_primaria == mensagem_secundaria:

                    print(f"\n{True}")
                
                else:

                    print(f"\n{False}")
            
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