#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
while True:
	print
	import math
	a = float(raw_input("Lado A: "))
	b = float(raw_input("Lado B: "))
	c = float(raw_input("Lado C: "))
	delta = (b ** 2) - 4 * a * c
	if a == 0: print "Não é uma equação de segundo grau, pois o valor de A é zero."
	else:
		if delta < 0: print "A equação não possui raízes reais, pois o delta é negativo."
		elif delta == 0:
			x = -b + math.sqrt(delta)
			print "A equação possui uma raiz real: %.2f" % x
		elif delta > 0:
			x1 = -b - math.sqrt(delta)
			x2 = -b + math.sqrt(delta)
			print "A equação possui duas raízes reais: %.2f e %.2f" % (x1, x2)
