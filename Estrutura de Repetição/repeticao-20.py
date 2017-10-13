#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
while True:
	n = int(raw_input("Número: "))
	if n < 0 or n > 16: print "Limite do fatorial a números inteiros positivos e menores que 16."
	else:
		print "%d! = " % n,
		a = 1
		for i in range(n, 0, -1):
			a *= i
			print "%d ." % i,
		print "= %d" % a
