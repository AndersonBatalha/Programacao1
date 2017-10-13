#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder SIM a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]
respostas = []
for i in range(5):
	resposta = raw_input(perguntas[i])
	if resposta != "s" and resposta != "n": print "Responda apenas s ou n."
	elif resposta == "s": respostas.append("Sim")
	elif resposta == "n": respostas.append("Nao")
print "Respostas", respostas
if respostas.count("Sim") == 0 or respostas.count("Sim") == 1:
	print "O suspeito respondeu SIM a", respostas.count("Sim"),
	"perguntas. Portanto pode ser considerado Inocente."
elif respostas.count("Sim") == 2:
	print "O suspeito respondeu SIM a", respostas.count("Sim"),"perguntas. Portanto pode ser considerado Suspeito."
elif respostas.count("Sim") == 3 or respostas.count("Sim") == 4:
	print "O suspeito respondeu SIM a", respostas.count("Sim"),"perguntas. Portanto pode ser considerado Cúmplice."
else: print "O suspeito respondeu SIM a", respostas.count("Sim"), "perguntas. Portanto pode ser considerado Assassino."
