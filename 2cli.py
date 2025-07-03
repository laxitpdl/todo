import functions
import time

now = time.strftime("%a - %b %d , %Y %H:%M:%S")
print("Today's date and time is: " + now)

while True:
    user_action = input("enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            row = f'{index + 1}-{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            index = number - 1
            new_todo = input("enter the new todo: ") + "\n"
            todos[index] = new_todo
            functions.write_todos(todos)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            message = f"todo {todo_to_remove} was removed from the list"
            print(message)
        except (ValueError, IndexError):
            print("not enough todos. Please enter a valid todo number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("wrong command")

print("bye!")
