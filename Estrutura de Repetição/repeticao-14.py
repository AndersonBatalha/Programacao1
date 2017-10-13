#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
while True:
	pares = 0
	impares = 0
	print
	for i in range(1, 11):
		numero = float(raw_input("Número %s: " % str(i).rjust(2)))
		if numero % 2 == 0:
			pares += 1
		else:
			impares += 1
	print "\nPares: %d\tÍmpares: %d" % (pares, impares)
