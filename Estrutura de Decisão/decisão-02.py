#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
while True:
	numero = float(raw_input("Número: "))
	if numero > 0:
		print "Positivo."
	elif numero < 0:
		print "Negativo."
	else:
		print "Zero."
