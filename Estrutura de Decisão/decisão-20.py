#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
soma = 0
for i in range(1, 4):
	nota = float(raw_input("Nota %d: " % i))
	soma += nota
	media = soma / 3
print "Soma das notas: %.2f" % soma
if media == 10: print "Aprovado com Distinção. Média: %.2f" % media
elif media >= 7: print "Aprovado. Média: %.2f" % media
else: print "Reprovado. Média: %.2f" % media
