"""
Faça um programa para imprimir de acordo com a imagem abaixo para um n
informado pelo usuário. Use uma função que receba um valor n inteiro e
imprima até a n-ésima linha.
"""

def funcao(num):
    for i in range(1,num+1):
        for c in range(1,i+1):
            print (i, end=' ')
        print()
num = int(input('Digite um número positivo: '))
if num > 0:
    funcao(num)
else: 
    print('Digite um número positivo!!!')