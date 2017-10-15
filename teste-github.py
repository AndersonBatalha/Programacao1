#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ("Este é um teste.")

def operacoes(tipo, n1, n2):
	if tipo == "soma":
		return "Soma:\t %d + %d = %d" %(n1,n2,n1+n2)
	elif tipo == "sub":
		return "Subtração:\t %d + %d = %d" %(n1,n2,n1-n2)
	elif tipo == "div":
		return "Divisão:\t %d + %d = %d" %(n1,n2,(n1+0.0)/n2)
	elif tipo == "mult":
		return "Mutliplicação:\t %d + %d = %d" %(n1,n2,n1*n2)

print operacoes("div", 2, 10)
