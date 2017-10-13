#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
while True:
	sexo = raw_input("Sexo: ")
	if sexo == "m" or sexo == "M":
		print "M - Masculino."
	elif sexo == "f" or sexo == "F":
		print "F - Feminino."
	else:
		print "Sexo inválido."
