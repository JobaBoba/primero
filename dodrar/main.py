import PySimpleGUI as sg
import patoolib
import os

sg.theme('DefaultNoMoreNagging')  # Выбор темы оформления

layout = [
    [sg.Text('Select a RAR archive to extract')],
    [sg.InputText(key='archive_path'), sg.FileBrowse(file_types=(('RAR Files', '*.rar'),))],
    [sg.Text('Select the output folder')],
    [sg.InputText(key='output_folder'), sg.FolderBrowse()],
    [sg.Button('Extract'), sg.Button('Exit')],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progress')],
]

window = sg.Window('RAR Archive Extractor', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Extract':
        archive_path = values['archive_path']
        output_folder = values['output_folder']

        if archive_path and output_folder:
            try:
                progress_bar = window['progress']
                progress_bar.UpdateBar(0)
                patoolib.extract_archive(archive_path, outdir=output_folder, interactive=False)
                sg.popup('Extraction Successful', 'Archive extracted successfully!')
            except Exception as e:
                sg.popup_error(f'Extraction Error: {str(e)}')

window.close()
