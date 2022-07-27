# Fazer basicamento todos os mecanismos de um calculador e depois quando tudo estiver rodando liso fazer um GUI usando o pysimplegui 
# falar oque cada mecanismos faz usando # obrigatorio 
# exemplo
# pede o primeiro numro:
# pede qual operador sera ultilizado 
# pede outro valor:
# Retorna com o calculo ja feito
    # isto em um loop

# Bibliotecas ultilizadas
import math as mt


cont_sair = 0


while True:
    
    print('* Multiplicaçao\n+ Adiçao \n- Subtraçao\n/ Divisao\n// Raiz Quadrada')
    opera = str(input('Escolha um: '))
    
    if opera == '//':
        raiz_quadradad = int(input('Qual raiz deseja saber: '))
        raiz = mt.sqrt(raiz_quadradad)
        print(f'A Raiz Quadrada de {raiz_quadradad} e  {raiz}')
        cont_sair += 1
        continue

    num1 = float(input('Primeiro Numero: '))
    num2 = float(input('Segundo Numero: '))

        
    if opera == '*':
        mult = (num1 * num2)
        print(f' A multiplicaçao dara: {num1} * {num2} == {mult}')
        cont_sair += 1
    elif opera == '+' or 'adiçao':
        adic = (num1 + num2)
        print(f'A soma dara: {num1} + {num2} == {adic}')
        cont_sair += 1 
    if opera  == '-':
        subtr =  (num1 - num2)
        print(f'A subtraçao dara: {num1} - {num2} == {subtr}')
        cont_sair += 1
    elif opera == '/':
        divi = (num1 / num2)
        print(f'A divisao dara {num1} / {num2} ==  {divi}')
        cont_sair += 1
    if cont_sair == 3:
        saida = str(input('Deseja sair: '))
        if saida == 'sim':
            break
        else:
            cont_sair = 0
            continue
