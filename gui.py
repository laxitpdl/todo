



import functions              # ✅ Correct import for functions module
import PySimpleGUI as sg      # ✅ Correct GUI module

                              # Layout with a label and an input box
label = sg.Text("Type in a to-do for today:")
input_box = sg.InputText(tooltip="Enter a to-do item here", key = "todo")  # ✅ Input box for to-do items
add_button = sg.Button("Add")  # ✅ Button to add a to-do item
# Window layout
window = sg.Window('To-Do App', 
                   layout=[[label], [input_box, add_button]], 
                   font=('Helvetica', 20))

while True:
    event, values = window.read()  # ✅ Read the window events and values
    print(event)  # ✅ Print the event and values for debugging
    print(values)  # ✅ Print the values for debugging
    
    match event:  # ✅ Use match-case for event handling
        
        
        case "Add":
            todos = functions.get_todos()  # ✅ Get the current list of to-dos
            new_todo = values["todo"] + "\n"  # ✅ Get the new to-do item from input box
            todos.append(new_todo)  # ✅ Add the new to-do item to the list
            functions.write_todos(todos)  # ✅ Write the updated list of to-dos to the file
        

        case sg.WIN_CLOSED:  # ✅ Handle window close event
            break  # ✅ Exit the loop if the window is closed







window.close()  # ✅ Close the window when done








#window.read()  # ✅ Read the window events
#window.close()
