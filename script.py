# Bibliotecas ultilizadas
import math as mt
from time import sleep

# Apenas um contador para quando o sistema der um que 2 loops (Podemos almentar ou diminuir a frequencia)
contador_saida = 0

# Loop
while True:
    try:
        # Painel de operçoes possiveis
        print('* Multiplicaçao\n+ Adiçao \n- Subtraçao\n/ Divisao\n// Raiz Quadrada')
        operaçoes = str(input('Escolha um: '))

        if operaçoes == '//': # Raiz Quadrada
            raiz_quadradad = float(input('Qual raiz deseja saber: '))
            raiz = mt.sqrt(raiz_quadradad)
            print(f'A Raiz Quadrada de {raiz_quadradad} e  {raiz}')
            contador_saida += 1
            continue
        
        # Si nao for uma Raiz Quadrada ele pede dois numero para calcular
        num1 = float(input('Primeiro Numero: '))
        num2 = float(input('Segundo Numero: '))
    # Caso aja algum erro 
    except: 
        print('ERRO, Algo esta errado')
        contador_saida = 0
        sleep(1)
        continue
    else:

        if operaçoes == '*': # Multiplicaçao
            mult = (num1 * num2)
            print(f' A multiplicaçao dara: {num1} * {num2} == {mult}')
            contador_saida += 1
        elif operaçoes == '+' : # Adiçao
            adic = (num1 + num2)
            print(f' A soma dara: {num1} + {num2} == {adic}')
            contador_saida += 1 
        elif operaçoes  == '-': # Subtraçao
            subtr =  (num1 - num2)
            print(f' A subtraçao dara: {num1} - {num2} == {subtr}')
            contador_saida += 1
        elif operaçoes == '/': # Divisao
            divi = (num1 / num2)
            print(f' A divisao dara {num1} / {num2} ==  {divi}')
            contador_saida += 1

        if contador_saida == 2: # Sistema de saida 
            saida = str(input('Deseja sair: ')[0])
            if saida == 's':
                break
            else:
                contador_saida = 0
                continue

