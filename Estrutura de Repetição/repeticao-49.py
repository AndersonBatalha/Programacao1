#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 49. Faça um programa que mostre os n termos da Série a seguir:
# a.   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.
n = 0
m = -1
a = 0
b = 0
print "S =",
while m < 100:
	n += 1
	m += 2
	a += n
	b += m
	print "(%d / %d) +" % (n, m),
print "\n\nS = %d / %d" % (a, b)
