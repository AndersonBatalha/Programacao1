#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
while True:
	numero = float(raw_input("Número: "))
	if round(numero) == numero:
		print "Inteiro"
	else:
		print "Decimal"
