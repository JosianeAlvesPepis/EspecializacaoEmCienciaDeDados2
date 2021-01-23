"""
Faça um programa em Python 3 que leia da entrada padrão uma linha com 3 valores 
separados por espaços em branco e retorne a computação da operação aritmética 
indicada pelo primeiro valor sobre os outros dois.

- O primeiro valor é um único carácter indicando a operação: +, - e * (soma, 
subtração e multiplicação);
- O segundo e terceiro valores são inteiros.

A sua saída deve ser uma única linha com o resultado da operação.

Dica:
Uma maneira de fazer a leitura é:
op, a, b = input().split()
a = int(a)
b = int(b)

"""

op, a, b = input().split()
a = int(a)
b = int(b)

if op == '+':
  print(a+b)
elif op == '-':
  print(a-b)
elif op == '*':
  print(a*b)
elif op == '/':
  print(a/b)
elif op == '//':
  print(a//b)  
elif op == '%':
  print(a%b)
elif op == '**':
  print(a**b)  
  