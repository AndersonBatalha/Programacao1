#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = raw_input("Nome: ")
senha = raw_input("Senha: ")
while nome == senha:
	print "Nome não pode ser igual a senha."
	nome = raw_input("Nome: ")
	senha = raw_input("Senha: ")
else:
	print "Válido."
