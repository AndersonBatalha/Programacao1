#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 11 - Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
# 15 / 10 / 1994
# 01 2 34 5 6789
data = extenso = ''
meses = []
def data_por_extenso(data, extenso):
	meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	data = raw_input("Data: ")
	if len(data[6:10]) != 4:
		print "O formato deve ser: DD/MM/AAAA."
	else:
		extenso = "%s de %s de %s" % (data[0:2], meses[int(data[3:5]) - 1], data[6:10])
		return extenso
while True:
	print data_por_extenso(data, extenso)
