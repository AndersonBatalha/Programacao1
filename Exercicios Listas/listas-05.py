#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
numeros = []
pares = []
impares = []
npares = 0
nimpares = 0
for i in range(1, 7):
	numero = int(raw_input("Número %d: " % i))
	numeros.append(numero)
	if numeros[i - 1] % 2 == 0:
		npares += 1
		pares.append(numero)
	elif numeros[i - 1] % 2 == 1:
		nimpares += 1
		impares.append(numero)
print "\nNúmeros:", numeros, "\nÍmpares:", impares, "\nPares:", pares
