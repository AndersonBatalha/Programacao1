#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
# FULANO
# FULAN
# FULA
# FUL
# FU
# F

lista = []
nome = raw_input("Nome: ")
for i in range(len(nome)):
    lista.append(nome[i])

while len(lista) > 0:
	for i in range(len(lista)):
		print lista[i],
	lista.pop()
	print "\n"
