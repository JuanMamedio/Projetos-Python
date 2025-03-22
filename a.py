nome = input('Digite seu nome')
idade = input('digite sua idade')
peso = float(input('digite seu peso'))
altura = float(input('digite sua altura'))

imc = peso/(altura*altura)

print('Olá', nome, 'aos', idade, 'anos seu imc é', imc)
