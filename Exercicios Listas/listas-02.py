#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
numeros = []
for i in range(10):
	n = float(raw_input("Número %d: " % (i + 1)))
	numeros.append(n)
print "Números: em ordem inversa:",
numeros.reverse()
print numeros
