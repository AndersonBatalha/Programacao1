#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa para imprimir:
# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
numero = 0
n = 0
def imprime_numeros(numero):
	n = 0
	numero = int(raw_input("Número: "))
	for i in range(numero):
		n += 1
		print "%5s" % str(n) * n
while True:
	print imprime_numeros(numero)
