#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
# paisA = 40000 paisB = 200000
# taxaA = 3 / 100.0 taxaB = 1.5 / 100.0
paisA = int(raw_input("População do país A: "))
paisB = int(raw_input("População do país B: "))
taxaA = float(raw_input("Taxa de crescimento do país A (em %): "))
taxaB = float(raw_input("Taxa de crescimento do país B (em %): "))
i = 0
while paisA <= 10000000 or paisB <= 10000000:
	paisA += paisA * taxaA
	paisB += paisB * taxaB
	i += 1
	print "Ano %d\tPaís A: %.2f\tPaís B: %.2f" % (i, paisA, paisB)
print "\nForam necessários %d anos para a população do país A ultrapassasse ou igualasse a população do país B, mantidas as taxas de crescimento." % i
