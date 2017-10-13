#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# a. Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120
n = int(raw_input("Número: "))
print "Fatorial de %d" % n
print "%d! = " % n,
a = 1
for i in range(n, 0, -1):
	a *= i
	print ". %d" % i,
print "= %d" % a
