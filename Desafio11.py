#Faça um programa que leia a altura e largura, e mostre o quanto de litro de tinta sera gasto
# Uma lata de 1 litro pinta 2m^2

Altura = float(input('Qual a altura da parede?'))

Largura = float(input('Qual a Largura da parede?'))

Tamanho_Parede = Altura*Largura

Quantidade_lata = Tamanho_Parede/2

print(f'Olá, você precisa de {Quantidade_lata:.0f} latas, para pintar sua parede')

