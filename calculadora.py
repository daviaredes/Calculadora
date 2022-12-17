from PySimpleGUI import *

theme('DarkGrey14')

layout = [
    [
        [Text('', key='tela')],
        [Txt('' * 10)]
    ],
    [
        ReadFormButton('C'),
        ReadFormButton('<<')
    ],
    [
        ReadFormButton('1'),
        ReadFormButton('2'),
        ReadFormButton('3'),
        ReadFormButton('+')
    ],
    [
        ReadFormButton('4'),
        ReadFormButton('5'),
        ReadFormButton('6'),
        ReadFormButton('-')
    ],
    [
        ReadFormButton('7'),
        ReadFormButton('8'),
        ReadFormButton('9'),
        ReadFormButton('*')
    ],
    [
        ReadFormButton('/'),
        ReadFormButton('0'),
        ReadFormButton('.'),
        ReadFormButton('=')
    ]
]

Wind = FlexForm('Calculadora', default_button_element_size=(5, 2), auto_size_buttons=False, layout=layout)

Resultado = ''

while True:

    button, values = Wind.Read()

    if button == 'C':
        Resultado = ''
        Wind.find_element('tela').update(Resultado)
    elif button == '<<':
        Resultado = Resultado[:-1]
        Wind.find_element('tela').update(Resultado)    
    elif button == '=':
        calculo = eval(Resultado)
        calculo = str(round(float(calculo)))
        Wind.find_element('tela').Update(calculo)
        Resultado = calculo
    if button == 'Quit' or button == None:
        break
    else:
        Resultado += button
        Wind.find_element('tela').Update(Resultado)
