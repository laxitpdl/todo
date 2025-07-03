#1
#user_text = input("Enter a todo: ") ||input function is designed to print outits argument on the commandline also able to get input from user and return taht user input. 
#print(user_text)

#2
#user_prompt = "Enter a todo: "
#text = input(user_prompt)
#print(text)

#print("Enter todo:")
#user_text = input()
#print(user_text)

#user_prompt = "Enter a todo: "
#todo1 = input(user_prompt)
#todo2 = input(user_prompt)
#todo3 = input(user_prompt)

#todos = [todo1, todo2, todo3]  #[]=python list
#print(todos)
#print(type(user_prompt)) #type() helps to know the type of variable

#book_title = input("Enter Title: ")
#book_title = len(book_title)
# print("the length of the title is", book_title)

#user_prompt = "enter a todo: "
#while True:                            #while loop  #true is boolean
    #todo = input(user_prompt)
    #print(todo)
    #print("next.................")   ||THIS CODE OVER WRITES SO 


#user_prompt = "enter a todo: "
#todos = []                             #||#THIS IS DONE AND :
#while True:
    #todo = input(user_prompt)
    #todos.append(todo)               #||#.append uses to add item in the end of the list
    #print(todos)
    
        
#password = input("Enter password: ")
#while password != "pass123":            #!= means not equal to 
    #password = input("Enter agian: ")

#print("Passord is corret!")


#countries = []

#while True:
    #country = input("Enter the country: ")
    #countries.append(country)
    #print(countries)
    
    
#todos = []                                                  #this todos are printed in one line ["", ""] like this!
#while True:
#    user_action = input("Type add, show, or exit: ")
    
#    match user_action:                               #||match variable
#        case "add":                                    # when add this keeps on asking one by one and when pressed show it shows by combining all add and when pressed exit it breaks the loop and prints bye!
#            todo = input("enter a todo: ")
#            todos.append(todo)
#        case "show":                                   #this shows the add todos by combining all
#            print(todos)
#        case "exit":
#            break                              #thius breaks the loop
#print("bye!")                                  #and prints bye!         

        
#todos = []                                      #this prints todo in different lines
#while True:
#    user_action = input("enter add, show, or exit: ")
#    user_action = user_action.strip()                   #strip() command help to clean the command spaces 
#    match user_action:
#        case "add":
#            todo = input("enter a todo: ")          # |= is a operator which is operate show or display
#            todos.append(todo)
#        case "show" | "display"
#            for item in todos:                 #for loop
#                print(item)                    #for loop
#        case "exit":
#            break       
#         case _:
#             print("wrong command")
#print("bye!")



#todos = []                                     
#while True:
#    user_action = input("enter add, show, edit, complete or exit: ")
#    user_action = user_action.strip()
#    match user_action:                   
#        case "add":
#            todo = input("enter a todo: ") + "\n"  #\n is used to add new line in the end of the string
#            todos.append(todo)
#            file = open("extra.txt", "w")    #open() function is used to open a file in read, write or append mode.
#            file.writelines(todos)  #writelines() method is used to write a list of strings to a file.
#        case "show":
#            for index, item in enumerate(todos):  # enumerate() basically add 0, 1, 2 ,3 in list :is used to loop over something and have an automatic counter.
#                item = item.title()           #title() capitalize the first letter only in each output line. 
#                #print(index, "-", item)
#                row = f'{index+1}.{item}'      #+1= list starts with 0 so 1 bata suru hos bhanera   #f'{index}.{item}' is a formatted string literal (f-string) that allows you to embed expressions inside string literals, using curly braces {}.
#                print(row)                 # Display each todo with the first letter capitalized
#        case "edit":
#            number = int(input("Number of the todo to edit ?: ")) # int converts string or float to integer
#            number = number - 1                                   #python list from 0 so -1 is used to get the correct number
#            new_todo = input("Enter a new todo: ")
#            todos[number] = new_todo
#        case "complete":    
#            number = int(input("Number of the todo to complete ?: "))
#            todos.pop(number-1)
#        case "exit":
#            break       
#print("bye!")
            
#todos = []                                     
#while True:
#    user_action = input("enter add, show, edit, or exit: ")
#    user_action = user_action.strip()
#   match user_action:                   
#        case "add":
#            todo = input("enter a todo: ")
#            todos.append(todo)
#        case "show":
#            for item in todos:
#               item = item.title()  
#                print(item)                                     # Display each todo with the first letter capitalized        
#        case "edit":
#            edit = input("enter todo to edit: ")
#            if edit in todos:
#                index = todos.index(edit)                    #index() method returns the index of the first occurrence of a specified value in a list.
#                new_todo = input("enter new todo: ")
#                todos[index] = new_todo 
#            else:
#                print("todo not found")    
#        case "exit":
#            break       
#print("bye!")               




                 #we dont need to use list here because we are using file to store the todos
                 # This code is used to manage a todo list using a file to store the todos.
#todos = []       because we have extra.txt file to store the todos
                 #we can use file to store the todos in a file and read it later


#def get_todos(filepath="todo-app/extra.txt"):  # def function is used for repetitive tasks, so that we can call it whenever we need it.
#    """Read the todos from a file and return them as a list."""   #docstring is used to describe the function and its purpose.
   # This function reads the todos from a file and returns them as a list.
    
#    with open(filepath, "r") as file_local:     #with statement is used to open a file and automatically close it after the block of code is executed.
#            todos_local = file_local.readlines()                  ##readlines() method reads all the lines in a file and returns them as a list.
#    return todos_local
#return statement is used to return the value of todos_local to the caller of the function.
# This function is used to read the todos from the file and return them as a list.    


#todos_arg = get_todos()   non default parameters before default parameter todo_arg is non def # This line is commented out because we are not using it now. It was used to get the todos from the file.
#def write_todos(todos_arg, filepath="todo-app/extra.txt")  :       #it needs to know what to write in the file i.e todo so todo_arg and its filepath  # This function is used to write the todos to the file.
#    """Write the todos to a text file."""
    # This function takes a list of todos and writes them to a file.
    
#    with open(filepath, "w") as file_local:  #with statement is used to open a file and automatically close it after the block of code is executed.
#        file_local.writelines(todos=todos_arg)     #writelines() method is used to write a list of strings to a file.
# no return statement is needed here because we are writing the todos to the file, not returning anything.






#from functions import get_todos, write_todos  # Importing the functions from the functions.py file
#form file import functions  # Importing the functions module



import functions  # Importing the functions module
import time  # Importing the time module to add a delay in the program



now = time.strftime("%a - %b %d , %Y %H:%M:%S")  # Getting the current date and time in a specific format
print("Today's date and time is: " + now)  # Printing the current date and time


while True:
    user_action = input("enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()
                                       #user_action = user_action.lower()  # This line is commented out because we are not using it now. It was used to convert the user input to lowercase.   

    
    
    
    
    
    
    if user_action.startswith('add'):  #or #and are boolean and exectuses both add and new if only add.... it wont work add new ....              
                                       #in is used to check if the user_action is in the case "add"  
                                       #match variable is used to match the user_action with the case "add"  
                                       #case is used to match the user_action with the case "add" for example match case "add": means if user_action is "add" then do the following code in the block.

        todo = user_action[4:]  
                                        #4: means to get the substring starting from index 4 to the end of the string. 
                                        #a=0 d=1 d=2 space =3 c=4 l=5 e=6 a=7 n=8 so it will start from c=4 and will get the rest of the string.    
                                        #input("enter a todo: ") + "\n"  #\n is used to add new line in the end of the string

                                        #file = open("todo-app/extra.txt", "r")   #todo-app is foler where extra.txt is  
                                        #open() function is used to open a file in read, write or append mode.
                                        #todos = file.readlines()                 
                                        #readlines() method reads all the lines in a file and returns them as a list.
                                        #file.close()                              

        todos = functions.get_todos() #functions (is module).get_todos() # This line is commented out because we are not using it now. It was used to get the todos from the file.
        
        todos.append(todo + '\n')  #append() method is used to add an item to the end of the list.

                                   #file = open("todo-app/extra.txt", "w")     
                                   #open() function is used to open a file in read, write or append mode.
                                   #file.writelines(todos)                  
                                   #writelines() method is used to write a list of strings to a file.
                                   #file.close()                            

        
        
        functions.write_todos(todos) #"todo-app/extra.txt")  # This line is commented out because we are not using it now. It was used to write the todos to the file.
        #write_todos() function is used to write the todos to the file. It takes

        # case add is used to add a new todo to the list and write it to the file.

    elif user_action.startswith('show'):
        

        todos = functions.get_todos() #with statement is used to open a file and automatically close it after the block of code is executed.
        

        # 1 way to remove the newline character from each item in the list
        #new_todos = []                               
        #for item in todos:
        #   new_item = item.strip("\n")                
        #   strip() method is used to remove the specified characters from the beginning and end of a string. Here, it removes the newline character "\n" from each item.
        #   new_todos.append(new_item)

        # 2 way to remove the newline character from each item in the list
        #new_todos = [item.strip('\n') for item in todos]  
        #list comprehension is used to create a new list by applying an expression to each item in the original list. 
        #Here, it removes the newline character "\n" from each item

        for index, item in enumerate(todos):  
            # enumerate() basically add 0, 1, 2 ,3 in list :is used to loop over something and have an automatic counter.
            item = item.strip("\n")           # 3 way to remove the newline character from each item in the list
            item = item.title()               #title() capitalize the first letter only in each output line. 
            #print(index, "-", item)
            row = f'{index+1}-{item}'          #+1= list starts with 0 so 1 bata suru hos bhanera   
            #f'{index}.{item}' is a formatted string literal (f-string) that allows you to embed expressions inside string literals, using curly braces {}.
            print(row) 
            # Display each todo with the first letter capitalized


    elif user_action.startswith('edit'):
        try: 
            #edit = input("enter todo to edit: ")  # This line is commented out because we are not using it now. It was used to get the todo to edit from the user.
            number = int(user_action[5:])  #5: means to get the substring starting from index 5 to the end of the string. e=0 d=1 i=2 t=3 space=4 number=5
            print(number)
            
            todos = functions.get_todos()#(filepath = "todo-app/extra.txt")  # This line is commented out because we are not using it now. It was used to get the todos from the file.

            index = number - 1  # Subtract 1 because list indexing starts at 0
            new_todo = input("enter the new todo: ") + "\n"  # Ask user for new todo and add newline

            todos[index] = new_todo  # Replace the old todo with the new one

            functions.write_todos(todo) #, filepath="todo-app/extra.txt")
        
        except  ValueError:
            print("Invalid input. Please enter a valid number.")
            user_action = input("enter add, show, edit, complete or exit: ")
            user_action = user_action.strip()
                  
            print("Invalid input. Please enter a valid number.")
            #user_action = input("enter add, show, edit, complete or exit: ")
            #user_action = user_action.strip()
            continue     


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])  
            #9: means to get the substring starting from index 9 to the end of the string. 
            #c=0 o=1 m=2 p=3 l=4 e=5 t=6 e=7 space =8 c=9 l=10 e=11 a=12 n=13 
            #so it will start from c=9 and will get the rest of the string.   

            #number = int(input("Number of the todo to complete ?: "))

            todos= functions.get_todos()

            index = number - 1  #indexing starts from 0, so we subtract 1 from the number entered by the user
            todo_to_remove = todos[index].strip('\n')  # Get the todo to be removed

            todos.pop(index)  # Remove the todo from the list

            functions.write_todos(todos) #, "todo-app/extra.txt")

            message = f"todo {todo_to_remove} was removed from the list"
            print(message)  # Print the message indicating which todo was removed
        
        except (ValueError, IndexError):
            print("not enough todos . Please enter a valid todo number.")
            user_action = input("enter add, show, edit, complete or exit: ")
            user_action = user_action.strip()
            continue
    
    
    elif user_action.startswith('exit'):
        break  

    else:
        print("wrong command")    

    print("bye!")
