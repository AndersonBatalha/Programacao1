#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor
cor = " "
class bola:
	def __init___(self):
		self.cor = True
		self.circunferencia = True
		self.material = None
	def troca_cor(self, cor):
		cor = raw_input("Informe a cor da bola: ")
		self.cor = cor
	def mostra_cor(self):
		cor = bola()
		return self.cor
