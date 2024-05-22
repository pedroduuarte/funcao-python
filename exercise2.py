"""
Reverso do número. Faça uma função que retorne o reverso de um número
inteiro informado. Por exemplo: 127 -> 721.
"""

def reverso_numero(num): 
    n = str(num)
    inverted_n = n[::-1]
    print(inverted_n)
reverso_numero(157) 