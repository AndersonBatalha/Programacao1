#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
while True:
	ano = int(raw_input("Ano: "))
	if ano % 4 == 1: print "Não é bissexto"
	elif ano % 4 == 0: print "Ano bissexto"
