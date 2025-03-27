#Faça um programa que leia um número e em seguida mostre a sua tabuada na tela.

Numero_P_TABUADA = int(input('Digite um número'))
Limite_tabuada = int(input('Digite até qual multiplicação deve ir'))

for i in  range(1,Limite_tabuada+1):
    print(f'{Numero_P_TABUADA}x{i} = {Numero_P_TABUADA*i}')