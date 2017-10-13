#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(raw_input("Salário: "))
if salario <= 280:
	aumento = 20
	perc_aumento = 20.0/100
elif salario > 280:
	aumento = 15
	perc_aumento = 15.0/100
elif salario > 700:
	aumento = 10
	perc_aumento = 10.0/100
elif salario > 1500:
	aumento = 5
	perc_aumento = 5.0/100
valor_aumento = perc_aumento * salario
novo_salario = (perc_aumento * salario) + salario
print "\nSalário antes do reajuste: R$ %.2f\nPercentual de aumento: %.1f %%\nValor do aumento: R$ %.2f\nNovo salário (com o aumento): R$ %.2f\n" % (salario,aumento, valor_aumento, novo_salario)
