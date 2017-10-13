#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
while True:
	valor_hora = float(raw_input("Salário por hora: "))
	horas_mes = float(raw_input("Horas trabalhadas por mês: "))
	salario_bruto = valor_hora * horas_mes
	fgts = salario_bruto * 11.0/100
	sindicato = salario_bruto * 3.0/100
	inss = salario_bruto * 10.0/100
	if salario_bruto <= 900:
		print "Isento de desconto no Imposto de Renda"
		desconto_ir = 0
	elif salario_bruto <= 1500: desconto_ir = salario_bruto * 5.0/100 # 5 %
	elif salario_bruto <= 2500: desconto_ir = salario_bruto * 10.0/100 # 10 %
	else: desconto_ir = salario_bruto * 20.0/100 # 20 %
	descontos = desconto_ir + sindicato + inss
	salario_liquido = salario_bruto - descontos + fgts
	print "Folha de Pagamento"
	print "-" * 50
	print "(-) Desconto do Imposto de Renda: R$", desconto_ir
	print "Salário Bruto: R$", salario_bruto
	print "(-) INSS (10%): R$", inss
	print "(+) FGTS (11%): R$", fgts
	print "Total de descontos: R$", descontos
	print "Salário Liquido: R$", salario_liquido
	print "-" * 50
