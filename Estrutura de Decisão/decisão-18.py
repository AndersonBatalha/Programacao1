#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
while True:
	print "Informe dia mês e ano no formato dd/mm/aaaa\nd - dia / m - mes / a - ano"
	dia = int(raw_input("Dia: "))
	mes = int(raw_input("Mês: "))
	ano = int(raw_input("Ano: "))
	if (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12) and (ano >= 1 and ano <= 9999): print "Data válida."
	else: print "Data inválida"
