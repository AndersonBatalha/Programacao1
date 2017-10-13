#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.
frase = raw_input("Frase: ")
lista = []
for i in range(len(frase)):
	lista.append(frase[i])
print "A:", lista.count("a")
print "E:", lista.count("e")
print "I:", lista.count("i")
print "O:", lista.count("o")
print "U:", lista.count("u")
print "Total de vogais:", lista.count("a") + lista.count("e") + lista.count("i") + lista.count("o") + lista.count("u")
print "Espaços:", lista.count(" ")
