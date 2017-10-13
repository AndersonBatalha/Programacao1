#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
print "Algoritmo que lê o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A - álcool, G - gasolina), calcule e imprima o valor a ser pago pelo cliente.\nObs: o preço do litro da gasolina é R$ 2,50 e o preço do litro do álcool é R$ 1,90."
combustivel = raw_input("Álcool / Gasolina: ")
if combustivel == "a" or combustivel == "A":
	litros_alcool = float(raw_input("Litros de alcool: "))
	preco_alcool = litros_alcool * 1.9
	if litros_alcool < 20: desconto = 3.0/100
	else: desconto = 5.0/100
	desconto_alcool = preco_alcool * desconto
	total_alcool = preco_alcool - desconto_alcool
	print "Desconto: R$", desconto_alcool
	print "Total a ser pago: R$", total_alcool
elif combustivel == "g" or combustivel == "G":
	litros_gasolina = float(raw_input("Litros de gasolina: "))
	preco_gasolina = litros_gasolina * 2.5
	if litros_gasolina < 20: desconto = 4.0/100
	else: desconto = 6.0/100
	desconto_gasolina = preco_gasolina * desconto
	total_gasolina = preco_gasolina - desconto_gasolina
	print "Desconto: R$", desconto_gasolina
	print "Total a ser pago: R$", total_gasolina
else: print "Informe apenas A ou G !!"
