from verificacao import Verificacao
from Questao_1.pilha import Pilha

pilha_principal = Pilha()
pilha_auxiliar = Pilha()

variavel = "(((())"

if Verificacao.verificacao_geral(variavel):
    pilha_principal.incializacao_pilha(variavel)

    caractere_analisado = pilha_principal[-1]

print(pilha_principal.len())

while pilha_principal.len()!=0:

    for i in range(pilha_principal.len()-2, -1, -1):
        if caractere_analisado == ")" and pilha_principal[i] == "(":
            caractere_analisado = pilha_principal[i]
            pilha_principal.pop()
            pilha_principal.pop()
        
        elif caractere_analisado == ")" and pilha_principal[i] != "(":
            caractere_analisado = pilha_principal[i]
            pilha_auxiliar.add(pilha_principal[i])
            pilha_principal.pop()
        
        elif caractere_analisado == "(":
            caractere_analisado = pilha_principal[i]
            pilha_auxiliar.add(pilha_principal[i])
            pilha_principal.pop()
        
        continue
    
    if pilha_auxiliar.len() != 0:

        for item in pilha_auxiliar:
            pilha_principal.add(item)
        
            pilha_auxiliar.pop()
        
        
        




        
        

print(True)