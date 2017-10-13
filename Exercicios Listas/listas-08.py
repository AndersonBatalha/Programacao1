#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []
for i in range(1, 6):
	idade = int(raw_input("Idade da pessoa %d: " % i))
	altura = float(raw_input("Altura da pessoa %d: " % i))
	idades.append(idade)
	alturas.append(altura)
idades.reverse()
alturas.reverse()
print "\nIdades:", idades, "\nAlturas:", alturas
