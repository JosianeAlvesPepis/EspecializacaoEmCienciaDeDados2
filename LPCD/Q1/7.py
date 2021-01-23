"""
Faça um programa em Python 3 que leia uma linha contendo um número inteiro de 4 
dígitos e calcule a soma dos dígitos. Por exemplo para o número 1234 o resultado 
é 1 + 2 + 3 + 4 = 10

Dica:
Não converta todo o número como um único inteiro, ao invés acesse cada dígito 
separadamente e então coverta cada dígitos em inteiro.

valor = input()

digito0 = int(valor[0])

digito1 = int(valor[1])

"""

valor = input()
dig0 = int(valor[0])
dig1 = int(valor[1])
dig2 = int(valor[2])
dig3 = int(valor[3])

print(dig0 + dig1 + dig2+ dig3)
