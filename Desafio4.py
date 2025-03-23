#O Usuário vai digitar algo, e vamos responder em que tipo se classifica oque ele digitou.

Mensagem_Usuario = str(input('Digite alguma coisa!'))


#É Alpha?
Mensagem_Alpha = Mensagem_Usuario.isalpha()
# É Alpha Num? 
Mensagem_Alpha_Numerico = Mensagem_Usuario.isalnum()
# Qual o tipo?
Tipo_Mensagem = type(Mensagem_Usuario)

print(f"A Mensagem é Alpha? {Mensagem_Alpha} ")
print(f"A Mensagem é Alpha Numerica? {Mensagem_Alpha_Numerico} ")
print(f"Qual o tipo da Mensagem? {Tipo_Mensagem} ")
