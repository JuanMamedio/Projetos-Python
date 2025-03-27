#Faça um programa que leia o salario de um funcionario, e mostre o novo salario com 15% de reajuste.

Salario_atual = float(input('Digite o salario atual'))
Novo_salario = Salario_atual*1.15

print(f'Olá, o seu salario agora é R$ {Novo_salario:.2F}')