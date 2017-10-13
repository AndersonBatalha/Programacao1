#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 13 - Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
def moldura(min = 1, max = 20):
	escolha = raw_input("Escolha o caracter (+, -, |)")
	linhas = int(raw_input("Número de linhas: "))
	colunas = int(raw_input("Número de colunas: "))
	if escolha == "+":
		if (linhas < 1 or linhas > 20) or (colunas >)
	elif escolha == "-":
	elif escolha == "|":
	else:
		print "Inválido"
