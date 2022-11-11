# Classe MiniPilha
class miniPilha:

    # Método construtor
    def __init__(self):
        self.__estrutura = []

    
    # Método para adicionar algum objeto a pilha
    def push(self, objeto):
            
        self.__estrutura.append(objeto)

        print("\nNúmero adicionado com sucesso!!!\n")
        
    
    # Método para remover algum objeto a pilha
    def pop(self):

        # Se a pilha estiver vazia
        if not self.__estrutura:

            print("\nA pilha já está vazia!!!\n")
        
        else:
            
            self.__estrutura.pop()

            print("\nNúmero removido com sucesso!!!\n")
    

    # Método que retorna o objeto mais recente que foi adicionado
    def top(self):
        
        try:

            return f"\nNÚMERO NO TOP DA PILHA = {self.__estrutura[-1]}\n"
        
        except:

            return "Não há nenhum número na pilha!!!"
    

    # Método que retorna o objeto de menor valor dentro da pilha
    def getMin(self):

        try:

            # Declarando uma variavel que armazenará o menor objeto da pilha
            menor = self.__estrutura[-1]

            # Para cada número dentro da pilha
            for numero in self.__estrutura:

                # Se o número for menor que o menor número no momento
                if numero < menor:

                    # A variavel menor recebe como valor esse número
                    menor = numero
            
            # Retorna a variavel menor
            return f"\nMENOR NÚMERO DA PILHA = {menor}\n"
        
        except:

            return "\nNão há nenhum número na pilha!!!\n"
    

    def __str__(self):
        
        saida = ""

        for index, numero in enumerate(self.__estrutura):

            saida += f"Elemento {index + 1} = " + str(numero) + "\n"
        
        return saida


