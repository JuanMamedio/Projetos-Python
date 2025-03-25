#Faça um aplicativo que some 4 notas trimestrais e calcule a média dessas notas:
try:

    Nota_1trimestre = float(input('Digite a nota do primeiro trimestre'))
    Nota_2trimestre = float(input('Digite a nota do segundo trimestre'))
    Nota_3trimestre = float(input('Digite a nota do terceiro trimestre'))
    Nota_4trimestre = float(input('Digite a nota do quarto trimestre'))
    Bonus_Atividade = float(input('Digite a nota bonus das atividade'))

    Nota_PROVAS = (Nota_1trimestre+Nota_2trimestre+Nota_3trimestre+Nota_4trimestre)/4 
    Nota_Final = Nota_PROVAS+Bonus_Atividade

    print(f'Ola Aluno, Sua nota final é {Nota_Final:.2f}')


    if Nota_Final >= 6:
        print('Parabens, você foi aprovado')
    else:
        print('Poxa vida, você foi reprovado')

except ValueError:
    print('Digite somente números, animal')