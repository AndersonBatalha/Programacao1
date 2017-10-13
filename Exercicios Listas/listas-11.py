#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
a = []
b = []
c = []
for i in range(1, 11):
	n1 = int(raw_input("Número %d: " % i))
	a.append(n1)
print
for i in range(1, 11):
	n2 = int(raw_input("Número %d: " % i))
	b.append(n2)
print
for i in range(1, 11):
	n3 = int(raw_input("Número %d: " % i))
	c.append(n3)
print "\nA:", a, "\n\nB:", b, "\n\nC:", c, "\n\nD:", a + b + c
