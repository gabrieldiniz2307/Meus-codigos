# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GZCg0ZjXQgJpw1I5HEVp3Hn2-Mm2mAsF
"""

def valorPagamento(prestacao, taxa_juros, dias_atraso):
    multa = 0.03 * dias_atraso
    pagamento = prestacao * (1 + taxa_juros/100)
    total = prestacao + pagamento
    return pagamento, total

total_pagamentos = 0
total_valores = 0

while True:
    prestacao = float(input("Me informe o valor da prestação : "))

    if prestacao == 0:
        print("Relatório do dia:")
        print("Total de pagamentos:", total_pagamentos)
        print("Total de valores:", total_valores)
        print("Programa encerrado.")
        break
    dias_atraso = int(input("Me informe o número de dias em atraso: "))

    pagamento, total = valorPagamento(prestacao, dias_atraso)

print("Valor do pagamento:", pagamento)
print("Valor total:", total)

total_pagamentos += pagamento
total_valores += total



