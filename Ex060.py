# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

numero = int(input('Digite um número para ver seu fatorial: '))
c = numero
fatorial = factorial(numero)

while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    c = c - 1

print(fatorial)
