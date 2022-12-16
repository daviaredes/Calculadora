from PySimpleGUI import *

theme('DarkGrey14')

layout = [
    [
        Text('', key='tela')
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
        ReadFormButton(','),
        ReadFormButton('=')
    ]
]

Wind = FlexForm('Calculadora', default_button_element_size=(5, 2))
Wind.Layout(layout) 

Result = ''

while True:

    button, values = Wind.Read()

    if button == 'C':
        Result = ''
        Wind.find_element('tela').update(Result)
    elif button == '<<':
        Result = Result[:-1]
        Wind.find_element('tela').update(Result)
        
    if button == 'Quit' or button == None:
        break