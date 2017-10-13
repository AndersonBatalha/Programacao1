#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
notas = []
soma = 0
for i in range(1, 3):
	nota = float(raw_input("Nota %d: " % i))
	while nota > 10 or nota < 0:
		print "Inválido!!"
		nota = float(raw_input("Nota %d: " % i))
	else:
		notas.append(nota)
		soma += nota
		media = soma / 2
if media == 10: print "Aprovado com distinção."
elif media >= 7: print "Aprovado. Média: %.2f" % media
else: print "Reprovado. Média: %.2f" % media
