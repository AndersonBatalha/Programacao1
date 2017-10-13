#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
while True:
	base = int(raw_input("Base: "))
	expoente = int(raw_input("Expoente: "))
	print "%d elevado a %d é %d." % (base, expoente, base ** expoente)
