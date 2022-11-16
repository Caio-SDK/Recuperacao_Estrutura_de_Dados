# Bibliotecas utilizadas
from validacao import Validacao
from Questao_3.mini_pilha import miniPilha

import os
import sys


# Variável que guardará as opções do menu
opcoes_do_menu = """
[ 1 ] = Adicionar um elemento a pilha
[ 2 ] = Pegar o menor ele elemento da pilha atualmente
[ 3 ] = Remover um elemento da pilha
[ 4 ] = Pegar o elemento mais recente da pilha
[ 5 ] = Exibir a pilha neste momento
[ 6 ] = Voltar para o menu anterior
[ 7 ] = Sair do programa
"""

# Criação de um objeto da classe MiniPilha
pilha = miniPilha()


# Classe Menu
class MenuQuestao3:

    #  Método estático para a criação do menu principal da questão 3
    @staticmethod
    def menu_principal_questao_3():

        while True:

            # Exibição das opções
            print(opcoes_do_menu)

            # Requisitando uma opção desejada ao usuário
            opcao = Validacao.ValidacaoNumeroInteiro("Digite sua opção: ")

            # Limpando o terminal para não haver poluição visual
            os.system("cls")

            # Opção 1
            if opcao == 1:

                # Requisitando um número desejado pelo usuário a ser adicionado a pilha
                numero_desejado = Validacao.ValidacaoNumeroInteiro("Digite o número que deseja adicionar a pilha: ")

                # Adicionando o número a pilha
                pilha.push(numero_desejado)
            
            # Opção 2
            elif opcao == 2:

                # Exibição do menor número da pilha
                print(pilha.getMin())
            
            # Opção 3
            elif opcao == 3:

                # Remoção do número mais recente adicionado a pilha
                pilha.pop()
            
            # Opção 4
            elif opcao == 4:

                # Exibição do número mais recente adicionado a pilha
                print(pilha.top())
            
            elif opcao == 5:

                print(pilha)

            # Opção 6
            elif opcao == 6:

                # Fim do laço de repetição para voltar ao menu anterior
                break
                
            # Opção 7
            elif opcao == 7:

                # Saindo do programa
                sys.exit()
            
            # Opção inválida
            else:

                print("\nDigite uma opção válida!!!\n")