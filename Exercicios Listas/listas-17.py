#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m / Segundo Salto: 6.1 m / Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m / Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
nomes = []
saltos = []
while True:
	nome = raw_input("Nome do atleta: ")
	if len(nome) > 0:
		for i in range(1, 6):
			salto = float(raw_input("Salto %d: " % i))
			saltos.append(salto)
		media = sum(saltos) / len(saltos)
		nomes.append(nome)
	else:
		if len(nomes) == 0:
			print "Sem atletas cadastrados."
		else:
			print "Encerrado"
			for i in range(len(nomes)):
				print "\nAtleta: %s" % nomes[i]
			for i in range(len(saltos)):
				for i in range(len(saltos)):
					print "Salto %d: %.2f m" % (i + 1, saltos[i])
			print "Média dos saltos: %.2f m" % media
			break
