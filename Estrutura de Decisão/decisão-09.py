#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
while True:
	n1 = float(raw_input("Número 1: "))
	n2 = float(raw_input("Número 2: "))
	n3 = float(raw_input("Número 3: "))
	if n1 > n2 and n1 > n3:
		if n3 > n2: print n1, n3, n2
		else: print n1, n2, n3
	elif n2 > n1 and n2 > n3:
		if n1 > n3: print n2, n1, n3
		else: print n2, n3, n1
	elif n3 > n1 and n3 > n2:
		if n1 > n2: print n3, n1, n2
		else: print n3, n2, n1
