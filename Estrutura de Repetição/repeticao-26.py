#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
while True:
	ncandidatos = int(raw_input("\nNúmero de candidatos: "))
	votos = []
	candidatos = []
	percentual = []
	for i in range(1, ncandidatos + 1):
		nome = raw_input("Candidato %d: " % i)
		candidatos.append(nome)
	print "Candidatos:"
	for i in range(ncandidatos):
		print "%d - %s" % (i + 1, candidatos[i])
		votos.append(0)
	neleitores = int(raw_input("\nNúmero de eleitores: "))
	for i in range(1, neleitores + 1):
		voto = int(raw_input("Voto do eleitor %d: " % i))
		while voto > len(candidatos):
			voto = int(raw_input("Voto do eleitor %d: " % i))
		else:
			votos[voto - 1] += 1
	for i in range(len(votos)):
		perc = ((votos[i] + 0.0) / (sum(votos) + 0.0)) * 100
		percentual.append(perc)
	print "Resultado Final:\n#\tNome\t\tNúmero de votos\t\tPercentual"
	for i in range(ncandidatos):
		print "%s %s %s votos %s %%" % (str(i + 1).ljust(7), candidatos[i].ljust(10), str(votos[i]).rjust(7), str(percentual[i]).rjust(19))
