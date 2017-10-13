#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
a = []
b = []
for i in range(1, 11):
	n1 = int(raw_input("Número %d: " % i))
	a.append(n1)
print
for i in range(1, 11):
	n2 = int(raw_input("Número %d: " % i))
	b.append(n2)
print "\nA:", a, "\nB:", b, "\nC (A + B):", a + b
