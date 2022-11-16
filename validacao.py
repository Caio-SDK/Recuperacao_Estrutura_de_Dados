# Bibliotecas utilizadas
import sys


# Classe Validação
class Validacao:
    # Definição de um método estático para validação de números inteiros
    @staticmethod
    def ValidacaoNumeroInteiro(mensagem):

        while True:

            try:

                # Entrada de um número inteiro
                numero_inteiro = int(input(mensagem))

                # Retorna o número
                return numero_inteiro

            except (KeyboardInterrupt):

                # Caso o usuário encerre o programa de maneira inadequada
                print("\n\nObrigado por teste!!!\n")
                sys.exit()

            except:

                print("Por favor digite um número inteiro válido!!!")