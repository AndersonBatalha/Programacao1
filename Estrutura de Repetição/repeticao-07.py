#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 7. Faça um programa que leia 5 números e informe o maior número.
numeros = []
for i in range(1, 6):
	numero = float(raw_input("Número %d: " % i))
	numeros.append(numero)
print "%d é o maior número." % (max(numeros))
