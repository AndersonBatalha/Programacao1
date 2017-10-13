#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vogais = 0
consoantes = 0
palavra = raw_input("Informe uma palavra: ")
for letra in palavra:
	if palavra not in "aeiou": consoantes =+ 1
	else:
		vogais += 1
print "A palavra %s tem %d vogais e %d consoantes." % (palavra, vogais, consoantes)
