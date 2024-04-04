"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
name = input('Digite seu nome: ')

if len(name) <= 4:
    print(f'Olá, {name}. Seu nome possui {len(name)} letras, e é considerado curto.')

elif (len(name) == 5) or (len(name) == 6):
    print(f'Olá, {name}. Seu nome possui {len(name)} letras, e é considerado normal.')

else:
    print(f'Olá, {name}. Seu nome possui {len(name)} letras, e é considerado grande.')