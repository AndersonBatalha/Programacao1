#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 24.  Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
import random
numeros = []
n = []
for i in range(1, 101):
	numeros.append(random.randint(1, 6))
print "Números:",
for i in range(len(numeros)):
	print "%d" % (numeros[i]),
print "\n"
for i in range(1, 7):
	print "Número %d: %d vezes" % (i, numeros.count(i))
	n.append(numeros.count(i))
print "\nTotal:", sum(n)
