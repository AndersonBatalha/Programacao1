#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
while True:
	numero = int(raw_input("Número: "))
	if numero < 1000:
		n = str(numero)
		if len(n) == 3: print "%s centenas, %s dezenas e %s unidades." % (n[0], n[1], n[2])
		elif len(n) == 2: print "%s dezenas e %s unidades." % (n[0], n[1])
		else: print "%s unidades." % n[0]
	else: print "Informe um número entre 0 e 1000."
