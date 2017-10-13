#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
while True:
	print
	n = int(raw_input("Número de pessoas: "))
	idades = []
	for i in range(1, n + 1):
		idade = int(raw_input("Pessoa %d: " % i))
		idades.append(idade)
	print "Idades:",
	for i in range(len(idades)):
		print idades[i],
	media = sum(idades) / len(idades)
	if media >= 0 and media <= 25: turma = "Jovem"
	elif media >= 26 and media <= 60: turma = "Adulta"
	else: turma = "Idosa"
	print "\nMédia de idade de %.2f anos. A turma é %s." % (media, turma)
