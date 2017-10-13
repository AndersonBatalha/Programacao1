#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numeros = []
soma = 0
multiplicacao = 1
for i in range(1, 6):
	numero = int(raw_input("Número %d: " % i))
	numeros.append(numero)
	soma += numero
	multiplicacao *= numero
print "\nNúmeros:",
for i in range(1, 6):
	print numeros[i - 1],
print "\nSoma: %d\nMultiplicação: %d" % (soma, multiplicacao)
