#!/usr/bin/env python3
# _*_ coding: utf8 _*_
# cont.py - Primeiro Programa

"""
Importa o módulo randon e sorteia
um número inteiro entre 1 e 100
"""

import random
numero = random.randint(1, 100)
escolha = 0
tentativas = 0
while escolha != numero:
    escolha = int(input("Escolha um numero entre 1 e 100:"))
    tentativas += 1
    if escolha < numero:
        print("O numero", escolha, "e menor que o sorteado.")
    elif escolha > numero:
        print("O numero", escolha, "e maior que o sorteado.")

print("Parabens voce acertou com", tentativas, "tentativas.")            
