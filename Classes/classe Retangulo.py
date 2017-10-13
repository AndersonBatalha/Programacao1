#!/usr/bin/env python
# -*- coding: utf-8 -*-
class retangulo:
	ladoA = None
	ladoB = None
	def __init__(self, ladoA, ladoB):
		self.ladoA = ladoA
		self.ladoB = ladoB
		print ("Criando instância Retangulo")
	def calcula_area(self):
		return self.ladoA * self.ladoB
	def calcula_perimetro(self):
		return 2 * self.ladoA + 2 * self.ladoB
from classe_retangulo import Retangulo
print (retangulo(1, 5))
