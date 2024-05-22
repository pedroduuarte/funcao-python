"""
Faça uma função que computa a potência de a
b para valores de a e b informados pelo usuário. Assuma valores de a e b como inteiros e não utilize
o operador ** ou funções da biblioteca Math.
"""

a = int(input('Digite a base: '))
b = int(input('Digite o expoente: '))
def pot (base,expoente): 
    if b == 0: return 1
    else: 
        potencia = 1 
        for i in range (1,b+1): 
            potencia *= a
        return potencia 
print(f'Potência de base {a} e expoente {b} = {pot(a,b)}') 