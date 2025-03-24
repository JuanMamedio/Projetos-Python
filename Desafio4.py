#O Usuário vai digitar algo, e vamos responder em que tipo se classifica oque ele digitou.
Mensagem_Usuario = str(input('Digite alguma coisa!'))
#É Alpha?
Mensagem_Alpha = Mensagem_Usuario.isalpha()
# É Alpha Num? 
Mensagem_Alpha_Numerico = Mensagem_Usuario.isalnum()
# Qual o tipo?
Tipo_Mensagem = type(Mensagem_Usuario)
# É maiuscula?
Mensagem_Maiusculo = Mensagem_Usuario.isupper()
#É minuscula?
Mensagem_Minusculo = Mensagem_Usuario.islower()

print(f"A Mensagem é Alpha? {Mensagem_Alpha} ")
print(f"A Mensagem é Alpha Numerica? {Mensagem_Alpha_Numerico} ")
print(f"Qual o tipo da Mensagem? {Tipo_Mensagem} ")
print(f'A mensagem é tudo em Maiuscula? {Mensagem_Maiusculo}')
print(f'A mensagem é tudo em minusculo? {Mensagem_Minusculo}')
