#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for i in range(4):
	nota = float(raw_input("Nota %d: " % (i + 1)))
	notas.append(nota)
soma = sum(notas)
media = soma / 4
print "Notas:",
for i in range(len(notas)):
	print notas[i], " ",
print "\nSoma das notas: %d\nMédia das notas: %.2f" % (soma, media)
