#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# a. Maior e Menor Acerto;
# b. Total de Alunos que utilizaram o sistema;
# c. A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A / 02 - B / 03 - C / 04 - D / 05 - E / 06 - E / 07 - D / 08 - C / 09 - B / 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
respostas = []
a = [] # respostas certas
b = [] # respostas erradas
acertos = 0
erros = 0
alunos = 0
while True:
	sair = raw_input("Digite as respostas em letra maiúscula\n\nResponda S (sim) ou N (não): Outro aluno vai utilizar o sistema? ")
	if sair == "N" or sair == "n":
		break
	elif sair == "S" or sair == "s":
		alunos += 1
		for i in range(1, 11):
			resposta = raw_input("Questão %d: " % i)
			respostas.append(resposta)
		for i in range(len(gabarito)):
			if gabarito[i] == respostas[i]:
				acertos += 1
			else:
				erros += 1
		a.append(acertos)
		b.append(erros)
		if "ABCDE" not in respostas:
			print "Digite respostas apenas de A a E!\n"
		else:
			print "Número de alunos: %d\nAcertos: %d\nErros: %d" % (alunos, acertos, erros)
	else: print "Digite apenas S ou N!"
