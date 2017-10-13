#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas
numeros = alturas = []
for i in range(1, 11):
	numero = int(raw_input("\nNúmero do aluno %d: " % i))
	altura = int(raw_input("Altura do aluno %d (em centímetros): " % i))
	numeros.append(numero)
	alturas.append(altura)
print "\n\nAluno mais alto:\nNúmero: %d\tAltura: %d cm\n\nAluno mais baixo:\nNúmero: %d\tAltura: %d cm" % (numeros[alturas.index(max(alturas))], max(alturas), numeros[alturas.index(min(alturas))], min(alturas))
