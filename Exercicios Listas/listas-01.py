#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
numeros = []
for i in range(5):
	n = float(raw_input("Número %d: " % (i + 1)))
	numeros.append(n)
print "Números:",
for i in range(len(numeros)):
	print numeros[i],
