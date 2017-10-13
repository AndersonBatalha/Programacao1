#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal;
print "Digite dois números e qual a operação desejada:\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação"
operacoes = ["Soma", "Subtração", "Divisão", "Multiplicação"]
escolha = int(raw_input("Qual a operação você deseja realizar: "))
n1 = float(raw_input("Número 1: "))
n2 = float(raw_input("Número 2: "))
for i in range(1):
	if escolha < 1 or escolha > 4:
		print "Número inválido."
		break
	else:
		print "A operação escolhida foi", operacoes[escolha - 1]
		if escolha == 1:
			soma = n1 + n2
			print n1, "+", n2, "=", soma
			if soma % 2 == 0: print "Par"
			else: print "Ímpar"
			if soma > 0: print "Positivo"
			else: print "Negativo"
			if round(soma) == soma: print "Inteiro"
			else: print "Decimal"
		elif escolha == 2:
			subtracao = n1 - n2
			print n1, "-", n2, "=", subtracao
			if subtracao % 2 == 0: print "Par"
			else: print "Ímpar"
			if subtracao > 0: print "Positivo"
			else: print "Negativo"
			if round(subtracao) == subtracao: print "Inteiro"
			else: print "Decimal"
		elif escolha == 3:
			divisao = n1 / n2
			print n1, ":", n2, "=", divisao
			if divisao % 2 == 0: print "Par"
			else: print "Ímpar"
			if divisao > 0: print "Positivo"
			else: print "Negativo"
			if round(divisao) == divisao: print "Inteiro"
			else: print "Decimal"
		else:
			multiplicacao = n1 * n2
			print n1, "x", n2, "=", multiplicacao
			if multiplicacao % 2 == 0: print "Par"
			else: print "Ímpar"
			if multiplicacao > 0: print "Positivo"
			else: print "Negativo"
			if round(multiplicacao) == multiplicacao: print "Inteiro"
			else: print "Decimal"
