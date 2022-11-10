# Classe Pilha
class Pilha:

    # Variável da classe que indica o número máximo de itens que uma pilha pode ter
    quantidade_maxima = 100

    # Método construtor
    def __init__(self):
        self.__estrutura = []
    

    def incializacao_pilha(self, expressao):

        for caracter in expressao:
            self.add(caracter)
        
        return self.__estrutura

    
    # Método para verificar se a pilha está vázia ou não
    def empty(self):

        if self.__estrutura:

            return False

        else:

            return True


    # Método para adicionar algum objeto a pilha
    def add(self, objeto):

        # Se a quantidade máxima for menor ou igual a quantidade total da pilha
        if self.quantidade_maxima <= len(self.__estrutura):

            print("A pilha está cheia")

        else:
            
            self.__estrutura.append(objeto)

    
    # Método para remover algum objeto a pilha
    def pop(self):

        if self.empty():

            print("A pilha já está vazia!!!")
        
        else:
            
            self.__estrutura.pop()
    

    def len(self):

        return len(self.__estrutura)

    
    # Método Dunder para a função print
    def __str__(self):

        # Declaração da variavel que armazenará os itens em formato de String
        itens_pilha = ""

        # Para cada item dentro da pilha
        for item in self.__estrutura:

            itens_pilha += str(item) + "\n"
        
        # Retornar os itens da pilha em formato de String
        return itens_pilha
    
    
    def __getitem__(self, key):
        
        if key == -1:
            return self.__estrutura[-1]

        return self.__estrutura[key]


if __name__ == '__main__':
    pilha = Pilha()
    pilha.incializacao_pilha("()))4(((5")
    print(pilha[-1])