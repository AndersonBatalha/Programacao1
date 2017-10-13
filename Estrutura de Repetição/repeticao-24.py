#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 24. Faça um programa que calcule o mostre a média aritmética de N notas.
while True:
	print
	n = int(raw_input("Número de notas: "))
	notas = []
	for i in range(1, n + 1):
		nota = float(raw_input("Nota %d: " % i))
		while nota < 0 or nota > 10:
			nota = float(raw_input("Nota %d: " % i))
		notas.append(nota)
	print "Notas:",
	for i in range(len(notas)):
		print notas[i],
	print "\nMédia: %.2f" % (sum(notas) / len(notas))
