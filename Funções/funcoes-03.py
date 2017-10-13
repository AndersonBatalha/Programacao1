#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
a = b = c = total = 0
def soma(a, b, c, total):
	a = int(raw_input("A: "))
	b = int(raw_input("B: "))
	c = int(raw_input("C: "))
	total = a + b + c
	print "%d + %d + %d =" % (a, b, c),
	return total
print soma(a, b, c, total)
