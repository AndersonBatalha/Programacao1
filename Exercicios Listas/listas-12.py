#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = []
alturas = []
alunos = 0
for i in range(1, 4):
	idade = int(raw_input("Idade do aluno %d: " % i))
	altura = float(raw_input("Altura do aluno %d: " % i))
	idades.append(idade)
	alturas.append(altura)
	mediaaltura = sum(alturas) / len(alturas)
	mediaidade = sum(idades) / len(idades)
for i in range(len(idades)):
	if idades[i] > 13 and mediaaltura < alturas[i]:
		alunos += 1
print "Média de altura: %.2f\nMédia de idade: %.1f\n%d alunos com mais de 13 anos possuem altura inferior à média de altura." % (mediaaltura, mediaidade, alunos)
