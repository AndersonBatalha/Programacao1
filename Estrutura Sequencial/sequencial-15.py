#!/usr/bin/env python
# coding: utf-8
# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
print ("Salario mensal.")
salario_hora = float (raw_input ("Quanto voce ganha por hora: "))
horas_trabalhadas = float (raw_input ("Quantas horas voce trabalha no mes: "))
salario_bruto = salario_hora * horas_trabalhadas
ir = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print ("O salario bruto e: %.2f R$") % salario_bruto
print ("O valor destinado ao Imposto de Renda e: %.2f R$") % ir
print ("O valor destinado ao INSS e: %.2f R$") % inss
print ("O valor destinado ao sindicato e: %.2f R$") % sindicato
print ("O total dos descontos e: %.2f R$") % descontos
print ("O salario liquido e: %.2f R$") % salario_liquido
