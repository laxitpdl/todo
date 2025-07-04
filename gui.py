import functions                # ✔ imports your own functions.py with get_todos() and write_todos()
import PySimpleGUI as sg        # ✔ imports PySimpleGUI to create GUI

# ✔ Label above the input box
label = sg.Text("Type in a to-do for today:")

# ✔ Input text box for user to type todos
input_box = sg.InputText(tooltip="Enter a to-do item here", key="todo")

# ✔ "Add" button
add_button = sg.Button("Add")

# ✔ Listbox shows current todos from the file using functions.get_todos()
list_box = sg.Listbox(values=functions.get_todos(),     # from functions.py → def get_todos(): reads list from file
                      key='todos', enable_events=True, size=(45, 10))

# ✔ Edit and Complete buttons
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# ✔ Main GUI window layout
window = sg.Window('To-Do App',
                        layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                      font=('Helvetica', 20))

# ✔ Event loop for reading actions like clicks or typing
while True:
    event, values = window.read()        # ✔ Read which button was clicked or input updated
    print(event)                         # ✔ Useful for debugging
    print(values)

    match event:

        case "Add":
            todos = functions.get_todos()           # ✔ Reads existing todos from file
            new_todo = values["todo"] + "\n"        # ✔ Gets input and adds newline
            todos.append(new_todo)                  # ✔ Adds it to the list
            functions.write_todos(todos)            # ✔ Writes updated list to file
            window['todos'].update(values=todos)    # ✔ Refreshes listbox in GUI

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]         # ✔ Gets selected item from listbox
                new_todo = values['todo'] + "\n"          # ✔ Gets edited text
                todos = functions.get_todos()             # ✔ Fetch current list
                index = todos.index(todo_to_edit)         # ✔ Find index of selected item
                todos[index] = new_todo                   # ✔ Replace old item with new text
                functions.write_todos(todos)              # ✔ Save to file
                window['todos'].update(values=todos)      # ✔ Update GUI list
            except:
                pass                                       # ✘ Avoids crash if nothing selected (can improve later)

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]     # ✔ Get selected item
                todos = functions.get_todos()             # ✔ Read current list
                todos.remove(todo_to_complete)            # ✔ Remove selected item
                functions.write_todos(todos)              # ✔ Save updated list
                window["todos"].update(values=todos)      # ✔ Refresh listbox
                window["todo"].update(value='')           # ✔ Clear input box
            except:
                pass                                       # ✘ Avoids crash if nothing selected
        

        case "Exit":
            break



        case 'todos':                                     # ✔ Triggered when item in listbox is clicked
            window['todo'].update(value=values['todos'][0]) # ✔ Put selected text into input box

        case sg.WIN_CLOSED:                               # ✔ Exit condition if window is closed
            break

window.close()                                             # ✔ Properly close the window after exit
