#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
while True:
	letra = raw_input("Letra: ")
	if letra in "aeiou": print "Vogal"
	else: print "Consoante."
