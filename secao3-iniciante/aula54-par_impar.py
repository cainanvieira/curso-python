"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

number = int(input("Digite um número inteiro: "))

if number % 2 == 0: 
    print('O número digitado é par')
else:
    print('O número digitado é ímpar')


