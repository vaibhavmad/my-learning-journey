import FreeSimpleGUI as kl

label1 = kl.Text('Enter Feet: ')
input_1 = kl.Input()

label2 = kl.Text('Enter Inches: ')
input_2 = kl.Input()

button_1 = kl.Button('Convert')

window = kl.Window('Converter',
                   layout=[
                       [label1, input_1],
                       [label2, input_2],
                       [button_1]
                   ])
window.read()
window.close()
