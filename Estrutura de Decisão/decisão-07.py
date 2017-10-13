#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
numeros = []
for i in range (1, 4):
	n = float(raw_input("Número %d: " % i))
	numeros.append(n)
print "Maior:", max(numeros), "\tMenor:", min(numeros)
