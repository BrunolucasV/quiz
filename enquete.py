from pickle import APPEND
from re import S

lista_numeros= [[3,2,2,4],[2,1,3,3],[2,3,1,4],[2,1,1,2],[1,3,1,3],[1,3,3,1],[2,2,1,3],[1,2,1,4],[2,2,1,2],[2,3,2,4],[1,3,3,2],[1,2,1,4]]
lista_nomes=["Baiken"],["Zed"],["Magda"],["Rosa"],["Fabel"],["Livesey"],["Catryn"],["Victor"],["Elena"],["Clint"],["Vessemir"],["Amelia"] #aqui seria onde voce colocaria as repostas do seu quiz 
usuario=[]
combinacao=0
resultado="deu"
numeros_perguntas=4
x =0 # ira compara um por um 
z=0 # ira compara um por um 
temp1 =0 # numero temporario ele sempre ira mudando para que a funçao ande para o proximo 
temp2 =0

pergunta=input(f"Há um oponente que é extremamente forte, o que você faria? \n 1 Procuraria forma uma aliança com outras pessoas para derrotá-lo \n 2 Procuraria me informar mais sobre ele para descobrir fraquezas \n 3 Iria enfeltrá-lo sozinho \n 4 Tentaria evitar lutar contra ele \n")
#use a funçao  if pergunta1.isnumeric():  caso queira garantir que entre apenas numeros validos 
pergunta= int(pergunta)
usuario.append(pergunta)

pergunta= input(f"\nUma pessoa pede por ajuda, o que você faria? \n 1 Eu pediria alguma coisa em troca \n 2 Daria uma arma para ela se vira \n 3 Eu ajudo sem pedir nada em troca \n 4 Eu a ignoro \n")
pergunta= int(pergunta)
usuario.append(pergunta)

pergunta= input("\nVocê encontra alguém com um item supervalioso que você precisa, o que você faria? \n 1 Eu o compraria \n  2 Eu sujeira uma competição valendo o item \n 3 Eu tentaria uma troca por outro item \n 4 Eu o roubaria \n")
pergunta= int(pergunta)
usuario.append(pergunta)

pergunta= input("\nQual a primeira coisa que você faz quando chega em uma cidade? \n 1 Procuro por pessoas precisando de ajuda \n 2 Uma boa taberna \n 3 Um cato para ficar isolado dos outros \n 4 Algum local para dormir \n")
pergunta= int(pergunta)
usuario.append(pergunta)

while temp2 < len(lista_numeros):
    contador = 0
    comparaçao = lista_numeros [temp2] #sera o numero a combinaçao a ser comparadada 
    while temp1 < numeros_perguntas:
            if usuario[temp1] == comparaçao[temp1]:
                contador += 1
                temp1 += 1
               # print(contador) caso voce queria ver se esta indo tudo certo 
                continue
            else:
                temp1 += 1
                continue
    if contador > combinacao:
        resultado = lista_nomes[temp2]
        combinacao=contador
        
    temp2+=1
    temp1=0

print (resultado)
    