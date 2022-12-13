from PySimpleGUI import PySimpleGUI as sg
from random import randint


def start_window():
    sg.theme('DarkGrey14')
    
    layout = [
        [
            sg.Text('' * 10),
            sg.Text('', k='tela', s=(5, 2)),
            sg.Text('' * 10)
        ],
        [
            sg.Button('//', k='potencia', s=(5, 2)),
            sg.Button('%', k='porcetagem', s=(5, 2)),
            sg.Button('C', k='clear', s=(5, 2)),
            sg.Button('<X', k='delet', s=(5, 2))
        ],
        [
            sg.Button('1', k='um' , s=(5, 2)), 
            sg.Button('2', k='dois', s=(5, 2)),
            sg.Button('3', k='tres', s=(5, 2)),
            sg.Button('+', k= 'mais', s=(5, 2))
        ],
        [
            sg.Button('4', k='quatro', s=(5, 2)),
            sg.Button('5', k='cinco', s=(5, 2)),
            sg.Button('6', k='seis', s=(5, 2)),
            sg.Button('- ', k='menos', s=(5, 2))
        ],
        [
            sg.Button('7', k='sete', s=(5, 2)),
            sg.Button('8', k='oito', s=(5, 2)),
            sg.Button('9', k='nove', s=(5, 2)),
            sg.Button('*', k='vezes', s=(5, 2))
        ],
        [
            sg.Button('/ ', k='divisao', s=(5, 2)),
            sg.ReadFormButton('0', k='zero', s=(5, 2)),
            sg.Button(',', k='virgula', s=(5, 2)),
            sg.ReadFormButton('=', k='igual', s=(5, 2))
        ]
    ]
    return sg.Window('start', layout=layout, finalize=True, resizable=True)

window1 = start_window()

Result = ''

def operaçoes():
    pass

while True:
    window, event, values = sg.read_all_windows()

    if window == window1 and event == sg.WINDOW_CLOSED:
        break

    if window == window1 and event == 'clear':
        Result = ''
        window.find_element('tela').update(Result)
        print('test botao clear')

    elif window == window1 and event == 'delet':
        Result == [-1]
        window.find_element('tela').update(Result)
        print('test botao delet')

