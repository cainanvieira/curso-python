"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
*As horas serão colocadas em números inteiros.
"""

hour = int(input("Informe a hora! "))

if hour >= 0 and hour <= 11:
    print("Olá, bom dia!")

elif hour >= 12 and hour <= 17:
    print("Olá, boa tarde!")

else:
     print("Olá, boa noite!")