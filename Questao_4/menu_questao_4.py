entrada = "3[ab]2[a]"

pilha_1 = []
pilha_2 = []
pilha_3 = []


ativador = False
ativ = False

for index in range(len(entrada)-1, -1, -1):

    if ativador and entrada[index] != "[":
        pilha_2.append(entrada[index])

    
    if ativ and entrada[index] != "]":
        string = ""
        for elemento in range(len(pilha_2)-1, -1, -1):
            string += pilha_2[elemento]
            pilha_2.pop()
        resultado = string*int(entrada[index])
        # print(resultado)
        for letra in resultado:
            pilha_3.append(letra)
        

    if entrada[index] == "]":
        ativador = True

        ativ = False
    
    elif entrada[index] == "[":
        ativ = True

        ativador = False


for i in range(len(pilha_3)-1, -1, -1):
    
    pilha_2.append(pilha_3[i])
    


print("".join(pilha_2))
    

    

# print(pilha_1)
# print(pilha_2)
# print(pilha_3)