



import functions  # ✅ Correct import for functions module
import PySimpleGUI as sg  # ✅ Correct GUI module

# Layout with a label and an input box
label = sg.Text("Type in a to-do for today:")
input_box = sg.InputText(tooltip="Enter a to-do item here")
add_button = sg.Button("Add")  # ✅ Button to add a to-do item
# Window layout
window = sg.Window('To-Do App', layout=[[label], [input_box, add_button]])


window.read()  # ✅ Read the window events
window.close()
