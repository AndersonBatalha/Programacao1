#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
numeros = []
n = []
for i in range(1, 6):
	numero = int(raw_input("Número %d: " % i))
	numeros.append(numero)
	n.append(numero ** 2)
print "\nNúmeros:", numeros, "\nSoma dos números:", sum(numeros), "\n\nNúmeros ao quadrado:", n, "\nSoma dos quadrados dos elementos do vetor:" , sum(n)
