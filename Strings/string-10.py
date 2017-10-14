#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

um_ate_vinte = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["zero", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

def numero_por_extenso(numero):
	if numero >= 0 and numero <= 99:
		if numero == 0:
			print "%d = %s" %(numero, dezenas[0])
		elif numero >= 1 and numero < 20:
			print "%d = %s" %(numero, um_ate_vinte[numero-1])
		else:
			string = str(numero)
			if int(string[1]) == 0:
				print "%d = %s" %(numero, dezenas[int(string[0])])
			else:
				print "%d = %s e %s" %(numero, dezenas[int(string[0])],um_ate_vinte[int(string[1])-1])

while True:
	n = int(raw_input("\nNúmero: "))
	if n < 0 or n > 99:
		print "Digite um número válido entre 0 e 99.\tTente novamente."
	else:
		numero_por_extenso(n)
