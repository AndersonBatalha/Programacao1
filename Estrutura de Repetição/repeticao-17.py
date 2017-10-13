#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
n = int(raw_input("Número: "))
a = 1
print "%d! = " % n,
for i in range(n, 0, -1):
	a *= i
	print "%d ." % i,
print "= %d" % a
