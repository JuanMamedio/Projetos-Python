#Escreve um programa que leia um numero em metros, e converta para CM, e Milimetros
Valor_Metro = float(input('Digite o Valor Metrico'))
Valor_CM = Valor_Metro*100
Valor_Mi = Valor_Metro*1000

print(f'Olá, a conversão de {Valor_Metro:.2f} Metros é, {Valor_CM:.2f} em CM e {Valor_Mi:.2f} em milimetros')

