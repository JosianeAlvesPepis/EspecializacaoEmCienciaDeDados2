"""
Leia 2 valores reais A e B, imprima a soma destes números na saída padrão com 
duas casas decimais.

Entrada:
Dois números reais A e B.

Saída:
Imprima uma linha com o valor da soma.

Dica:
Use 'float' para converter a string em número real
Use o código abaixo para gerar uma string contendo o valor do float 'resultado' 
com duas casas decimais
"{:.2f}".format(resultado)

"""

a, b = map(float,input().split())

print("{:.2f}".format(a+b))
