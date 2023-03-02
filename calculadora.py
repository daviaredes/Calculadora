from PySimpleGUI import *

theme('DarkGrey14')

menu_def = [['Menu', 'Historical']]

layout = [
    [
        [Menu(menu_def)],
        [Txt('' * 10)],
        [Text('0', key='screen', font='Helvetica, 20', size=(20, 3))],
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
],
Wind = FlexForm('Calculator', default_button_element_size=(9, 2), auto_size_buttons=False, layout=layout)

calculation_history = []
result = ''

while True:

    button, values = Wind.Read()

    if button == None:
        break
    else:
        result += button
        Wind.find_element('screen').Update(result)    

    if button == 'Historical':
        popup(calculation_history) 
    
    elif button == 'C':
        result = '0'
        Wind.find_element('screen').Update(result)
        result = ''

    elif button == '<<':
        result = result[:-3]
        Wind.find_element('screen').Update(result) 

    elif button == '=':
        calculation_history.append(result)
        calculation_system = eval(result[:-1])
        calculation_system = str(calculation_system)
        calculation_history.append(calculation_system)
        Wind.find_element('screen').Update(calculation_system)
        result = calculation_system
