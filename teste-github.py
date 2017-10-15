#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ("Este é um teste.")

def soma (a,b):
	return "%d + %d = %d" %(a,b,a+b)

print "Soma entre dois números:", soma(3,4)


def operacoes(tipo, n1, n2):
	if tipo == "soma":
		return "Soma:\t %d + %d = %d" %(n1,n2,n1+n2)
	elif tipo == "sub":
		return "Subtração:\t %d + %d = %d" %(n1,n2,n1-n2)
	elif tipo == "div":
		return "Divisão:\t %d + %d = %d" %(n1,n2,(n1/n2) + 0.0)
	elif tipo == "mult":
		return "Mutliplicação:\t %d + %d = %d" %(n1,n2,n1*n2)

print operacoes("div", 2, 10)

