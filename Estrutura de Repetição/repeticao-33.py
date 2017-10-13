#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
l = []
for i in range(len(meses)):
	temperatura = float(raw_input("Temperatura de %s (em ₒC): " % meses[i]))
	l.append(temperatura)
	media = sum(l) / len(l)
print "\nA média das temperaturas é de %.2f ₒC. A menor temperatura foi de %.2f ₒC em %s, e a maior temperatura foi de %.2f ₒC em %s." % (media, min(l), meses[l.index(min(l))], max(l), meses[l.index(max(l))])
