#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12 - Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
import random
palavra = " "
letras = []
def embaralha_palavra(palavra):
	palavra = raw_input("Palavra: ")
	for i in range(len(list(palavra))):
		letras.append(palavra[i])
		print letras
print embaralha_palavra(palavra)
