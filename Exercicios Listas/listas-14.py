#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]
respostas = []
while True:
	print "Informe apenas S ou N nas perguntas abaixo."
	for i in range(len(perguntas)):
		resposta = raw_input(perguntas[i])
		while resposta != "S" or resposta != "s" or resposta != "n" or resposta != "N":
			print "Informe apenas S ou N! Tente novamente!\n"
			resposta = raw_input(perguntas[i])
		respostas.append(resposta)
	if resposta == "S" or resposta == "N":
		if respostas.count("S") == 0 or respostas.count("S") == 1: s = "Inocente"
		elif respostas.count("S") == 2: s = "Suspeito"
		elif respostas.count("S") == 3 or respostas.count("S") == 4: s = "Cúmplice"
		elif respostas.count("S") == 5: s = "Assassino"
		print "\nVocê respondeu positivamente a %d questões, a pessoa é classificada como %s\n" % (respostas.count("S"), s)
