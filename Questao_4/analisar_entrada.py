# Classe Analisar Entrada
class AnalisarEntrada:

    #  Método para analisar e decodificar a string
    def analisar_mensagem(self, entrada):

        # Variáveis utilizadas
        numero_inicial_contagem = 0
        string = ''
        pilha = []

        # Para cada letra dentro da string que será dada como entrada
        for letra in entrada:

            if str(letra).isdigit():
                
                numero_inicial_contagem = numero_inicial_contagem * 10 + int(letra)

            elif letra == "[":

                pilha.append(string)
                pilha.append(numero_inicial_contagem)
                
                # Reiniciando as variaveis auxiliares
                string = ''
                numero_inicial_contagem = 0

            # Se a caractere analisado seja uma letra
            elif str(letra).isalpha():

                string += letra

            # # Se a caractere analisado seja igual a ]
            elif letra == ']':

                pre_num = pilha.pop()
                pre_string = pilha.pop()

                string = pre_string + pre_num * string

        return (string)
