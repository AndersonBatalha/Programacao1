#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
# Exemplo:
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
str1 = raw_input("String 1: ")
str2 = raw_input("String 2: ")
print "Compara duas strings."
print "String 1:", str1, "\nString 2:", str2
print "Tamanho de", str1, ":", len(str1), "\nTamanho de", str2, ":", len(str2)
if len(str1) == len(str2):
	print "Tem o mesmo comprimento."
else:
	print "Tem comprimentos diferentes."
if str1 == str2:
	print "São iguais no conteúdo."
else:
	print "Tem conteúdos diferentes."
