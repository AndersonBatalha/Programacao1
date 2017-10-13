#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
while True:
	turmas = int(raw_input("Número de turmas: "))
	total = 0
	nalunos = []
	for i in range(1, turmas + 1):
		alunos = int(raw_input("Número de alunos da turma %d: " % i))
		nalunos.append(alunos)
		while alunos > 40:
			alunos = int(raw_input("As turmas não podem ter mais de 40 alunos.\nNúmero de alunos da turma %d: " % i))
		else:
			total = sum(nalunos)
	else: print "Média de alunos: %.1f" % (total / turmas)
