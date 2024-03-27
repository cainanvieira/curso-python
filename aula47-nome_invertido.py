"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
       1 Seu nome é {nome} x
       2 Seu nome invertido é {nome invertido} x
       3 Seu nome contém (ou não) espaços x
       4 Seu nome tem {n} letras x
       5 A primeira letra do seu nome é {letra} x
       6 A última letra do seu nome é {letra}x

Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name = input('Digite seu nome: ')
age = input('digite sua idade: ')


if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')

    if ' ' in name:
        print(f'Seu nome contém espaços')
    else: 
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'A última letra do seu nome é {name[-1]}')

else:
    print('Desculpe, você deixou campos vazios')

