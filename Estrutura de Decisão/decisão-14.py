#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
soma = 0
numero_notas = int(raw_input("Número de notas: "))
for i in range(numero_notas):
	nota = float(raw_input("Nota: "))
	soma += nota
	media = soma / numero_notas
	if nota < 0 or nota > 10: print "Notas inválidas."
	else: print "Soma das notas: %.2f.\nMédia final do aluno: %.2f." % (soma, media)
if media >= 6 and media <= 10:
	if media >= 9: print "Conceito A"
	elif media >= 7.5: print "Conceito B"
	elif media >= 6: print "Conceito C"
	print "Aprovado"
else:
	if media >= 4: print "Conceito D"
	else: print "Conceito E"
	print "Reprovado"
