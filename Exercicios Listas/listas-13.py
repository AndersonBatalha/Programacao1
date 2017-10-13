#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
l = []
acima = []
for i in range(len(meses)):
	temperatura = float(raw_input("Temperatura de %s (em ₒC): " % meses[i]))
	l.append(temperatura)
	media = sum(l) / len(l)
for temperatura in l:
	if temperatura > media:
		acima.append(temperatura)
print "Meses em que a temperatura foi maior que a média atual:"
for i in range(len(acima)):
	print meses[l.index(acima[i])]
print "\nA média das temperaturas é de %.2f ₒC" % media
