#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 11. Altere o programa anterior para mostrar no final a soma dos números.
while True:
	n1 = int(raw_input("\nNúmero 1: "))
	n2 = int(raw_input("Número 2: "))
	a = 0
	if n1 == n2: print "Números iguais"
	elif n1 < n2:
		print "Números de %d a %d:" % (n1, n2)
		for i in range(n1, n2):
			print i,
			a += i
		print "\nSoma: %d" % a
	elif n1 > n2:
		print "Números de %d a %d:" % (n1, n2)
		for i in range(n1 + 1, n2 - 1, -1):
			print i,
			a += i
		print "\nSoma: %d" % a
