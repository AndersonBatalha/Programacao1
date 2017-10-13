#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# a. Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
while True:
	numero = int(raw_input("Número: "))
	print "Tabuada do %d" % numero
	for i in range(11):
		resultado = numero * i
		print "%d x %s = %d" % (numero, str(i).rjust(2), numero * i)
