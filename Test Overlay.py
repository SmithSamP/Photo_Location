import KML_Creator as ko
import PySimpleGUI as sg

sg.theme('Dark Grey 8')

sizes = ['Small', 'Medium', 'Large']

sizeDict = {
    'Small': 500,
    'Medium': 750,
    'Large': 1000
}

layout = [[sg.Text('Photo Folder')],
          [sg.Input(readonly=True, text_color='black'), sg.FolderBrowse(key='_IN_')],
          [sg.Input(readonly=True, text_color='black'), sg.FileSaveAs(default_extension='kml', key='_OUT_')],
          [sg.Checkbox("Create Image Icon   (May cause difficulty loading)", key='_ICON_')],
          [sg.Text('Photo Size')],
          [sg.Listbox(sizes, size=(20, 4), enable_events=False, default_values=['Medium'], key="_SIZE_")],
          [sg.OK(), sg.Cancel(key='_CANCEL_'), [sg.Text('', key='_STATUS_')]]]

window = sg.Window('Photo KML Generator', layout)

while True:
    event, values = window.read()
    inputFolder = values['_IN_']
    outputFile = values['_OUT_']
    icon = values['_ICON_']
    sizeList = values['_SIZE_']

    if event == sg.WIN_CLOSED or event == '_CANCEL_':
        break

    if event == 'OK':
        window['_STATUS_'].update('Working...')
        sizeInput = int(sizeDict[sizeList[0]])
        window['OK'].update(disabled=True)
        try:
            ko.run_KML(dirPath=inputFolder, savePath=outputFile, count=1, size=sizeInput, icon=icon)
        except FileNotFoundError:
            sg.popup_error(f'The path specified cannot be found')
        window['_STATUS_'].update('')

    window['OK'].update(disabled=False)

    f = open("error_logging.txt", "r")
    lines = f.readlines()
    f.close()
    d = open("error_logging.txt", "w")
    d.truncate(0)
    d.close()
    if len(lines) > 0:
        sg.popup_error(f'There are {len(lines)} photos without coordinates that have not been placed')

window.close()
