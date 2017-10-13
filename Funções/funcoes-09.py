#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 9 - Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
numero = 0
def numero_reverso():
	numero = int(raw_input("Número: "))
	n = str(numero)
	print n[::-1]
print numero_reverso()
