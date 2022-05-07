import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Bem vindo faça o login.')],
    [sg.Text('Usuario:'),[],sg.InputText(key='usuario',size=(25,1))],
    [sg.Text('Senha:'),[],sg.InputText(key='senha',password_char='*',size=(25,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de Login', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Matheus' and valores['senha'] == '123456':
            print('Bem-vindo! Matheus')
