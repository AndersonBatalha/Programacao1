#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.
numeros = []
for i in range(1, 6):
	numero = float(raw_input("Número %d: " % i))
	numeros.append(numero)
print "Soma: %.2f\nMédia: %.2f" % (sum(numeros), sum(numeros) / len(numeros))
