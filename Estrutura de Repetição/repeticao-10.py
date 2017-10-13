#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
while True:
	n1 = int(raw_input("\nNúmero 1: "))
	n2 = int(raw_input("Número 2: "))
	if n1 == n2: print "Números iguais"
	elif n1 < n2:
		print "Números de %d a %d:" % (n1, n2)
		for i in range(n1, n2):
			print i,
	elif n1 > n2:
		print "Números de %d a %d:" % (n1, n2)
		for i in range(n1, n2, -1):
			print i,
