#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
a = float(raw_input("Lado A: "))
b = float(raw_input("Lado B: "))
c = float(raw_input("Lado C: "))
if a + b > c or a + c > b or b + c > a:
	print "Os lados formam um triângulo."
	if a == b and a == c and b == c: print "Triângulo Equilátero: três lados iguais."
	elif (a == b or b == c or a == c) and (a != b or a != c): print "Triângulo Isósceles: quaisquer dois lados iguais."
	else: print "Triângulo Escaleno: três lados diferentes."
else: print "Os lados NÃO formam um triângulo."
