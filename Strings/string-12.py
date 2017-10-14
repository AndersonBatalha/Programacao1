#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

def corrigeTelefone(telefone):
	tel = list(telefone)
	print "\nTelefone sem formatação:", "".join(tel)
	if "-" in tel:
		tel.remove('-')
	if len(tel) != 8 or int(tel[0]) != 3:
		tel.insert(0, '3')
		tel.insert(4, '-')
	print "\nTelefone com formatação:","".join(tel)

corrigeTelefone('4610133')
