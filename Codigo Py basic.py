# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F2ixy7F3kkdmKzxlBaL10WMdrigVuONk
"""

#Exercicio 1
numero = int(input("Digite um número:"))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

#Exercicio 2
idade = int(input("Digite sua idade:"))

if idade >= 65:
    print("Você tem gratuidade no transporte")
else:
    print("Você não tem transporte gratuito")

#Exercicio 3
import numpy as np
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

notas = np.array([nota1, nota2])
media = np.mean(notas)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#Exercicio 4

preco_oculos = 200.00

idade = int(input("Digite sua idade:"))
if idade < 10:
  desconto = 10
elif idade > 80:
  desconto = 80
else: desconto = idade


valor_desconto = preco_oculos * (desconto / 100)
preco_total = preco_oculos - valor_desconto
print(f'Você recebeu um valor de desconto:{desconto} %')
print(f'O valor total a pagar é {int(preco_total)},00')

#Exercicio 5
salario_atual = float(input("Digite seu salário atual:"))
if salario_atual < 1500.00:
    aumento = 25
elif 1500.00 <= salario_atual < 1999.99:
    aumento = 20
elif 2000.00 <= salario_atual < 2999.99:
    aumento = 15
elif 3000.00 <= salario_atual < 4999.99:
    aumento = 10
else:
    if salario_atual >= 5000.00:
        aumento = 5
print(f'O valor do aumento é de {aumento} %')
print(f'O novo salário é de {int(salario_atual + (salario_atual * (aumento / 100)))}')
print(f'O salário reajustado é de {int(salario_atual)}')