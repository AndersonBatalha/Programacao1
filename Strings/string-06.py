#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
data = raw_input("Data: ")
meses = []
# 1 5 / 1 0 / 1 9 9 4
# 0 1 2 3 4 5 6 7 8 9
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print "Você nasceu no dia %s de %s de %s." % (data[0:2], meses[int(data[3:5]) - 1], data[6:10])
