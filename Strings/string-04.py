#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
# F
# FU
# FUL
# FULA
# FULAN
# FULANO
lista = []
nome = raw_input("Nome: ")
for i in range(len(nome)):
	lista.append(nome[i])
	print lista
