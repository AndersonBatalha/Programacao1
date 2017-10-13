#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
numeros = []
n = int(raw_input("Número de elementos do conjunto: "))
if n == 1: print "Inválido"
else:
	for i in range(1, n + 1):
		numero = int(raw_input("Número %d: " % i))
		while numero < 0 or numero > 1000:
			print "São aceitos apenas números entre 0 e 1000."
			numero = int(raw_input("Número %d: " % i))
		else:
			numeros.append(numero)
	print "Maior: %d\nMenor: %d\nSoma: %d" % (max(numeros), min(numeros), sum(numeros))
