#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5 --->> Começar por: 4 / Terminar em: 7
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20 / 5 X 5 = 25 / 5 X 6 = 30 / 5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
while True:
	numero = int(raw_input("\nNúmero: "))
	a = int(raw_input("A tabuada começa em: "))
	b = int(raw_input("A tabuada termina em: "))
	if a > b: print "O início não pode ser maior que o fim"
	else:
		print "\nVou montar a tabuada do %d começando em %d e terminando em %d:" % (numero, a, b)
		for i in range(a, b + 1): print "%d x %d = %d" % (numero, i, numero * i)
