import functions                    # I use this to read and write my todos from file
import PySimpleGUI as sg            # GUI library I use to create the app interface
import time                        # For showing the live clock

sg.theme("black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do for today:")
input_box = sg.InputText(tooltip="Enter a to-do item here", key="todo")
add_button = sg.Button("Add")


list_box = sg.Listbox(
    values=[todo.strip() for todo in functions.get_todos()],  # Remove '\n' from each todo before showing
    key='todos', enable_events=True, size=(35, 7)
)

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    'To-Do App',
    layout=[
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]
    ],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read(timeout=1000)
    # Update the clock every second
    window["clock"].update(value=time.strftime("%A - %b %d, %Y - %H:%M:%S"))

    match event:

        case "Add":
            todos = functions.get_todos()
            # When adding a todo, I clean input spaces and add '\n' for file format
            new_todo = values['todo'].strip() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            # When showing todos, I always strip '\n' so UI looks clean
            window['todos'].update([todo.strip() for todo in todos])  #window['todos'].update(todos)


        case "Edit":
            try:
                todo_to_edit = values['todos'][0]  # The selected todo without '\n'
                new_todo = values['todo'].strip() + "\n"  # Clean input, add newline

                todos = functions.get_todos()
                # My mistake before was using todos.index(todo_to_edit) directly,
                # which fails because todos have '\n' but selected todo does not.
                # So I strip todos and find index in cleaned list
                index = [t.strip() for t in todos].index(todo_to_edit)

                todos[index] = new_todo  # Replace old todo with new one
                functions.write_todos(todos)
                window['todos'].update([todo.strip() for todo in todos])
                window['todo'].update("")  # Clear input box

            except IndexError:
                sg.popup("ERROR: Select a task to edit first!", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]  # Selected todo without '\n'
                todos = functions.get_todos()

                # My previous mistake: I tried to remove todo_to_complete directly,
                # but todos have '\n', so remove() failed.
                # Now I filter todos keeping only those that don't match after stripping.
                todos.remove(todo_to_complete)
                #todos = [t for t in todos if t.strip() != todo_to_complete]

                functions.write_todos(todos)
                window['todos'].update([todo.strip() for todo in todos])
                window['todo'].update("")

            except IndexError:
                sg.popup("ERROR: Please select a task to complete.", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            # When I click a todo from listbox, I update input box for editing
            window['todo'].update(value=values['todos'][0])

window.close()
