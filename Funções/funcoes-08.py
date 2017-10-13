#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
numero = 0
def n_digitos(numero):
	numero = str(raw_input("Número: "))
	return "O número %d tem %d dígitos." % (int(numero), len(list(numero)))
print n_digitos(numero)
