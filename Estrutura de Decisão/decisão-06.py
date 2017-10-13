#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 6. Faça um Programa que leia três números e mostre o maior deles.
numeros = []
for i in range (3):
	n = float(raw_input("Número: "))
	numeros.append(n)
print "%d é o maior número" % max(numeros)
