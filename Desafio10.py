#Crie um programa que leia um saldo da carteira, e em seguida mostra quantos dollar a pessoa pode comprar.

Saldo_Atual = float(input('Qual teu saldo em R$, meu cria?'))

Dollar_Comercial = 5.74

Disponivel = Saldo_Atual*Dollar_Comercial

print(f'Olá, com {Saldo_Atual} em Reais, você pode comprar {Disponivel} Dollar')