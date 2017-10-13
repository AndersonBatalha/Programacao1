#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3. Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';
while True:
	nome = raw_input("\nNome: ")
	idade = int(raw_input("Idade: "))
	salario = int(raw_input("Salário: "))
	sexo = raw_input("Sexo: ")
	estado_civil = raw_input("Estado Civil: ")
	while len(nome) < 3 and (idade < 0 and idade > 150) and salario > 0 and (sexo != "m" and sexo != "f" and sexo != "M" and sexo != "F") and (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d" and estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D"):
		print "Inválido."
		nome = raw_input("Nome: ")
		idade = int(raw_input("Idade: "))
		salario = int(raw_input("Salário: "))
		sexo = raw_input("Sexo: ")
		estado_civil = raw_input("Estado Civil: ")
	else:
		print "Válido."
