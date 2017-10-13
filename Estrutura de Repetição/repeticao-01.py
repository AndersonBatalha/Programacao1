#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(raw_input("Nota: "))
while nota < 0 or nota > 10:
	print "Inválido."
	nota = int(raw_input("Nota: "))
else:
	print "Válido."
