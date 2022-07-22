# Fazer basicamento todos os mecanismos de um calculador e depois quando tudo estiver rodando liso fazer um GUI usando o pysimplegui 
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
    Num1 = int(input('Primeiro numero: '))
    opera = str(input('Escolha um\n * Multiplicaçao\n + Adiçao\n - Subtraçao\n / Divisao\n // Raiz Quadrada\n Qual sera a sua escolha: ').lower)
    Num2 = int(input('Segundo numero: '))
    cont_sair += 1
    
    if cont_sair == 3:
        sair = str(input('Deseja sair: ').lower)
        if sair == 'sim':
            print('Tchau   ')
            break    
    elif opera == '*' or 'multiplicaçao':
        mult = (Num1 * Num2)
        print(f'Multiplicando {Num1} e o {Num2} e igual {mult}')
        continue
    elif opera == '+' or 'adiçao':
        adic = (Num1 + Num2)
        print(f' Multiplicando {Num1} com {Num2} e igual {adic}')
        continue
    elif opera == '-' or 'subtraçao':
        subtr = (Num1 - Num2)
        print(f'Subtraindo {Num1} com {Num2} e igual {subtr}')
        continue
    elif opera == '/' or 'divisao':
        divis = (Num1 / Num2)
        print(f'Dividindo {Num1} com {Num2} e igual {divis}')
        continue
    elif opera == '//' or 'raiz quadrada':
        opeçao_raiz = int(input('Qual Raiz voce quer saber: '))
        raiz =  mt.sqrt(opeçao_raiz)
        print(f'A Raiz Quadrada de {opeçao_raiz}  e igual {raiz}')
        continue
