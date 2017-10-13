#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1 - Domingo, 2 - Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dias_da_semana = ["Inválido", "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
print "Informe um número correspondente ao dia da semana. (1-Domingo, 2- Segunda, etc.)"
for i in dias_da_semana:
	numero = int(raw_input("Número: "))
	if numero >= 1 and numero <= 7: print numero, "-", dias_da_semana[numero]
	else: print "O número não corresponde a um dia da semana. Tente novamente."
