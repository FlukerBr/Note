import PySimpleGUI as sg
import os

from PySimpleGUI.PySimpleGUI import Window
raiz = os.getcwd()
class app:
    def cria_note(self):
        with open(r'{0}\assets\notes\{1}.txt'.format(raiz, self.titulo), 'w', encoding='utf-8') as cn:
            cn.write('')
    def list_notes(self):
        n = ''
        notes = os.listdir(raiz + '/assets/notes')
        for line in notes:
            n += line + ' '
        notes = n.strip()
        notes = notes.replace('.txt', '')
        notes = notes.split()
        return notes
    def open_note(self):
        with open(r'{0}/assets\notes\{1}.txt'.format(raiz, self.note[0]), 'r', encoding='utf-8') as on:
            opennote = on.read()
        return opennote
    def modifica_note(self):
        with open(r'{0}\assets\notes\{1}.txt'.format(raiz, self.note[0]), 'w', encoding='utf-8') as mn:
            mn.write(self.mod_note)
    def telaopen(self):
        sg.theme('DarkTeal9')
        menu_m = [['Arquivo', ['Salvar']]]
        layout = [
            [sg.Menu(menu_m , key='menu')],
            [sg.Multiline(iniciar.open_note(), font=20, key='texto', size=(300, 18))],
            [sg.Button('Voltar', font=50, size=(10, 1))]
        ]
        window = sg.Window('Note', layout, size=(500, 400), icon='./assets/notes/icon.ico')
        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                exit()
            if value['menu'] == 'Salvar':
                self.mod_note = value['texto']
                iniciar.modifica_note()
            if event == 'Voltar':
                window.close()
                iniciar.main()
    def main(self):
        sg.theme('DarkTeal9')
        layout = [
            [sg.Text('Título :'), sg.Input(key='titulo', size=(20, 1)), sg.Button('Add', size=(5, 1))],
            [sg.Listbox(values=iniciar.list_notes(), size=(20, 20), key='-notes-'), sg.Button('Open')]
        ]
        window = sg.Window('Notes', layout, size=(350, 200), icon='./assets/notes/icon.ico')
        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Open':
                if value['-notes-'] != []:
                    self.note = value['-notes-']
                    window.close()
                    iniciar.telaopen()
            if event == 'Add':
                self.titulo = value['titulo']
                iniciar.cria_note()
            window['-notes-'].update(values=iniciar.list_notes())
iniciar = app()
iniciar.main()
