#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
while True:
	numeros = []
	n = int(raw_input("Número de elementos do conjunto: "))
	print
	if n == 1: print "Inválido"
	else:
		for i in range(1, n + 1):
			numero = int(raw_input("Número %d: " % i))
			numeros.append(numero)
		print "\nMaior: %d\nMenor: %d\nSoma: %d\n" % (max(numeros), min(numeros), sum(numeros))
