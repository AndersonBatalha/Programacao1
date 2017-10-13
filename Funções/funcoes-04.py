#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
numero = 0
def verifica_sinal(numero):
	numero = int(raw_input("Número: "))
	if numero > 0: return "P"
	elif numero < 0: return "N"
	else: return "0"
while True:
	print verifica_sinal(numero)
