import FreeSimpleGUI as sg


text1 = sg.Text('Enter Feet:')
text2 = sg.Text('Enter Inches:')

feet_input = sg.Input(tooltip='Enter Feet', key='feet')
inches_input = sg.Input(tooltip='Enter Inches', key='inch')

convert_button = sg.Button('Convert')

convert_output = sg.Text('', key='output')

layout = [[text1, feet_input], [text2, inches_input], [convert_button, convert_output]]
window = sg.Window('Converter', layout=layout, font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Convert':
             feet = int(values['feet'])
             inches = int(values['inch'])
             total_inches = inches + feet * 12
             total_meters = str(total_inches * 0.0254) + ' m'
             window['output'].update(total_meters)
        case sg.WIN_CLOSED:
            break

window.close()