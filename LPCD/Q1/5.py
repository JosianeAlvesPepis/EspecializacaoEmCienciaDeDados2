"""
Faça um programa em Python 3 que leia da entrada padrão uma linha com 1 valor 
inteiro, n. Imprima uma linha contendo a soma dos n primeiros valores inteiros 
positivos (inclusive o valor de n).

"""
n = int(input())
resultado = 0
contador = 0

while contador <= n:
    resultado += contador
    contador += 1

print(resultado)

