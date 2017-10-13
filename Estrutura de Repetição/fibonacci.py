#!/usr/bin/env python
# -*- coding: utf-8 -*-
while True:
	print
	valor = int(raw_input("Cálculo da Sequência de Fibonacci\nDigite o valor: "))
	a, b = 0, 1
	while b < valor:
		print b
		a, b = b, a+b
	print
