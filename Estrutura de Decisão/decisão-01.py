#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1. Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(raw_input("Número 1: "))
n2 = float(raw_input("Número 2: "))
if n1 > n2:
	print "O primeiro (%d) é maior." % n1
elif n1 < n2:
	print "O segundo (%d) é maior." % n2
else:
	print "%d e %d são iguais." % (n1, n2)
