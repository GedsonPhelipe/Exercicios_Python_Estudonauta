# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

n = int(input('Digite um número inteiro: '))
tot = 0

for c in range(1, n+1):
    if n % c == 0:
        tot = tot + 1

if tot == 2:
    print(f'O número {n} É PRIMO.')
    
else:
    print(f'O número {n} NÃO É UM NÚMERO PRIMO.')
