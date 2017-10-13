#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
precos = []
for i in range(1, 4):
	preco = float(raw_input("Preço do produto %d: " % i))
	precos.append(preco)
print "O mais barato é:", min(precos)
