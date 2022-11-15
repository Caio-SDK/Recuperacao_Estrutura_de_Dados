from Questao_1.pilha import Pilha


# Declaração de um objeto da class Pilha
pilha_principal = Pilha()
pilha_auxiliar = Pilha()


# Classe Verificadora
class Verificacao:


    @staticmethod
    def verificacao_geral(entrada):

        if Verificacao.verificar_quantidade_par(entrada) and Verificacao.verificar_primeiro_elemento(entrada) and Verificacao.verificar_ultimo_elemento(entrada) and Verificacao.verificar_quantidade_aberto_fechado:

            return True
        
        else:

            return False


    @staticmethod
    # Método para verificar se a entrada para a pilha contém uma quantidade de caracteres par
    def verificar_quantidade_par(entrada):

        # Se a quantidade de caracteres for impar ele retorna False
        return len(entrada)%2 != 0
 

    @staticmethod
    def verificar_primeiro_elemento(entrada):

        return entrada[0] in "])}"


    @staticmethod
    def verificar_ultimo_elemento(entrada):

        return entrada[-1] in "[({"


    @staticmethod
    def verificar_quantidade_aberto_fechado(entrada):

        quantidade_aberto = 0

        quantidade_fechado = 0

        for caracter in entrada:
            if caracter in "[({":
                quantidade_aberto += 1
            
            else:
                quantidade_fechado += 1
        
        return quantidade_fechado == quantidade_aberto

    
    

