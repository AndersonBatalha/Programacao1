#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
paisA = 100000
paisB = 200000
taxaA = 3 / 100.0
taxaB = 1.5 / 100.0
i = 0
print "Ano %d\tPaís A: %d\tPaís B: %d" % (i, paisA, paisB)
while paisA <= paisB:
	paisA += paisA * taxaA
	paisB += paisB * taxaB
	i += 1
	print "Ano %d\tPaís A: %d\tPaís B: %d" % (i, paisA, paisB)
print "\nForam necessários %d anos para a população do país A ultrapassasse ou igualasse a população do país B, mantidas as taxas de crescimento." % i
