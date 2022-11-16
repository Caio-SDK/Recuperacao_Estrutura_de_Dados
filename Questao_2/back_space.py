# Classe BackSpace
class BackSpace:
    
    #  Método estático para decodificar a mensagem
    @staticmethod
    def decodificar_mensagem(mensagem):

        # Pilhas utilizadas
        pilha_entrada = []
        pilha_saida = []

        # Declarando a variavel utilizada para contagem de caracteres apagados
        vezes_apagar = 0

        # Para cada caractere dentro da mensagem
        for caracter in mensagem:

            # Preenchendo a pilha de entrada
            pilha_entrada.append(caracter)

        # Para cada index dentro da pilha de entrada
        for index in range(len(pilha_entrada)-1, -1, -1):

            # Se o caractere daquele index for igual a #
            if pilha_entrada[index] == "#":

                vezes_apagar += 1
        
            # Se o caractere daquele index for diferente a #, ou seja, uma letra
            else:

                # Se a variavel de caractere apagado for igual a 0
                if vezes_apagar == 0:

                    # Adiciona a letra daquele index dentro da pilha de saida
                    pilha_saida.append(pilha_entrada[index])
                
                else:

                    vezes_apagar -= 1
            
            # Remover o elemento da pilha de entrada
            pilha_entrada.pop()

        # Para cada index dentro da pilha de saida
        for index in range(len(pilha_saida)-1, -1, -1):

            # Adicionar os elemento da pilha de saida na pilha de entrada
            pilha_entrada.append(pilha_saida[index])

            # Remover o elemento da pilha de saida
            pilha_saida.pop()

        
        # Retorna a mensagem codificada em forma de string
        return "".join(pilha_entrada)

