from Questao_1.verificacao import Verificacao

# Classe Analisar String
class AnalisarString:

    @staticmethod
    def analisar_string(entrada):

        # Verificando a entrada antes de ser analisada
        if Verificacao.verificacao_geral(entrada):

            # Declarando um objeto pilha
            pilha = []
            
            # Adicionando os elementos na pilha
            for item in entrada:
                
                """Verificando se o caractere atual é fechando, se for temos que atualizar que o anterior será sempre o ultimo da pilha(que terá os abrindo)
                e verificando se na lista tem algum elemento se não tiver já cai no falso pois indica que o primeiro elemento é algo fechando"""

                if item != '(' and item != '[' and item != '{' and len(pilha) > 0:

                    # Anterior passa a ser o último elemento da pilha
                    anterior = pilha[-1]
                    
                    # Anterior vai ser sempre abrindo então aqui verificamos se o item é fechando o ultimo caso não seja já retorna falso
                    if (item == ")" and anterior == "(") or (item == "]" and anterior == "[") or (item == "}" and anterior == "{"):

                        # Removendo um elemento da pilha
                        pilha.pop()
                        
                    # Retornando falso pois o ultimo não foi fechado
                    else:

                        return False
                    
                # Se for abrindo algo ele vai entrar na pilha para ser verificado no if de cima
                else:

                    pilha.append(item)
                    
            # Se a lista estiver vazia é porque todos foram abertos e fechados
            if len(pilha) == 0:

                return True
            
            else:

                return False

        else:

            return False