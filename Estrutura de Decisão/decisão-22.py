#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
while True:
	numero = int(raw_input("Número: "))
	if numero % 2 == 0: print "Par"
	else: print "Ímpar"
