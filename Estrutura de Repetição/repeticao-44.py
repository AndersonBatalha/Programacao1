#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato / O total de votos nulos / O total de votos em branco / A percentagem de votos nulos sobre o total de votos / A percentagem de votos em branco sobre o total de votos. /
# Para finalizar o conjunto de votos tem-se o valor zero.
candidatos = []
votos = []
for i in range(1, 5):
	candidato = raw_input("Candidato %d: " % i)
	candidatos.append(candidato)
	votos.append(0)
for i in range(2):
	votos.append(0)
l = ["Votos Nulos", "Votos em Branco"]
candidatos.append(l[0])
candidatos.append(l[1])
print "\nVotos para os respectivos candidatos:"
for i in range(len(candidatos)):
	print "%d - %s" % (i + 1, candidatos[i])
print "\nVote 0 para encerrar."
while True:
	voto = int(raw_input("Voto: "))
	if voto == 0:
		print "Votação encerrada."
		break
	else:
		if voto > len(votos) or voto < 0: print "Voto inválido."
		else:
			if voto >= 1 or voto <= 4:
				votos[voto - 1] += 1
				print votos
			else:
				l[voto - 1] += 1
print "#	Candidato		Votos		%"
for i in range(len(candidatos) - 2):
	perc = ((votos[i] + 0.0) / (sum(votos) + 0.0 - (votos[4] + votos[5]))) * 100
	print "%s	%s		%s		%.2f" % (i + 1, candidatos[i].rjust(10), str(votos[i]).rjust(3), perc)
print "\n%s: %d\n%s: %d" % (l[0], votos[4], l[1], votos[5])
