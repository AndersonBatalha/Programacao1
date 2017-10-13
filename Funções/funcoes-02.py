#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
numero = 0
n = 0
def imprime_numeros(numero):
	n = 0
	numero = int(raw_input("Número: "))
	for i in range(0, numero + 1):
		n += 1
		print n * i
while True:
	print imprime_numeros(numero)
