#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print "Informe o turno no qual você estuda: m - Manhã / t - Tarde / n - Noite"
while True:
	turno = raw_input("Turno: ")
	if turno == "m" or turno == "M": print "Bom dia!"
	elif turno == "t" or turno == "T": print "Boa tarde!"
	elif turno == "n" or turno == "N": print "Boa noite!"
	else: print "Inválido"
