#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
a = b = c = d = e = f = numero = 0
while numero >= 0:
	f += 1
	numero = int(raw_input("Número %d: " % f))
	if numero >= 0 and numero <= 25: a += 1
	elif numero >= 26 and numero <= 50: b += 1
	elif numero >= 51 and numero <= 75: c += 1
	elif numero >= 76 and numero <= 100: d += 1
	elif numero > 100: e += 1
else:
	print "\n[0 - 25]: %d números\n[26 - 50]: %d números\n[51 - 75]: %d números\n[76 - 100]: %d números\nNúmeros fora do intervalo entre 0 e 100: %d números" % (a, b, c, d, e)
