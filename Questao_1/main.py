from verificacao import Verificacao
from pilha import Pilha

pilha_principal = Pilha()
pilha_auxiliar = Pilha()

variavel = "(((())))))"

teste = 13

if Verificacao.verificacao_geral(variavel):
    pilha_principal.incializacao_pilha(variavel)

    caractere_analisado = pilha_principal[-1]

    while teste > 0:

        soma = ""
        for g in pilha_principal:
            soma += str(g) + ", "
        
        print(soma)

        for i in range(pilha_principal.len()-2, -1, -1):
            if caractere_analisado == ")" and pilha_principal[i] == "(":
                caractere_analisado = pilha_principal[i]

                pilha_principal.pop()
                pilha_principal.pop()

                print(f"INDEX {i} - Passou aquii")
                
            
            elif caractere_analisado == ")" and pilha_principal[i] != "(":
                caractere_analisado = pilha_principal[i]
                pilha_auxiliar.add(caractere_analisado)
                pilha_principal.pop()

                print(f"INDEX {i} - Passouuuuuuuuuuuuuuuuuuu")
            
            elif caractere_analisado == "(":

                if i == 0:
                    caractere_analisado = pilha_principal[i]
                    pilha_auxiliar.add(caractere_analisado)
                    pilha_principal.pop()

                    for item in range(pilha_auxiliar.len()-1, -1, -1):
                        pilha_principal.add(pilha_auxiliar[item])
                    
                        pilha_auxiliar.pop()
                    caractere_analisado = pilha_principal[-1]
                
                else:
                    caractere_analisado = pilha_principal[i]
                    pilha_auxiliar.add(caractere_analisado)
                    pilha_principal.pop()
            
                print(f"INDEX {i} - PGJGHFHGFHGFHGHGFHG")
            


            # COLCHETES VERIFICAION
            # if caractere_analisado == "]" and pilha_principal[i] == "[":
            #     caractere_analisado = pilha_principal[i]

            #     pilha_principal.pop()
            #     pilha_principal.pop()
                
            
            # elif caractere_analisado == "]" and pilha_principal[i] != "[":
            #     caractere_analisado = pilha_principal[i]
            #     pilha_auxiliar.add(caractere_analisado)
            #     pilha_principal.pop()
            
            # elif caractere_analisado == "[" and i == 0:
            #     caractere_analisado = pilha_principal[i]
            #     pilha_auxiliar.add(caractere_analisado)
            #     pilha_principal.pop()

            #     for item in range(pilha_auxiliar.len()-1, -1, -1):
            #         pilha_principal.add(pilha_auxiliar[item])
                
            #         pilha_auxiliar.pop()
            #     caractere_analisado = pilha_principal[-1]
                

            
            continue
        teste -= 1
    print(True)

else:

    print(False)

teste = 10


    
        


        