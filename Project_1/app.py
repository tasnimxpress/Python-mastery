# todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ").strip().capitalize()
            todo = todo + "\n"

            #read file
            file = open('Project_1/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            # write file
            file = open('Project_1/todos.txt', 'w') 
            file.writelines(todos)  
            file.close() 

        case 'show':
            file = open('Project_1/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            #use enumurate
            for index, item in enumerate(todos):
                print(f'{index + 1} {item.strip()}')
            
        case 'edit':
            file = open('Project_1/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            edit_option = int(input('Number of the todo to edit: '))
            position = edit_option - 1
            print(f'{todos[position].strip()}, will be modified')

            new_todo = input('Enter the new todo: ').capitalize()
            todos[position] = new_todo
            print('todos modified')

            file = open('Project_1/todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'complete':
            mark_complete = int(input('Number of the todo to mark completed: '))
            completed_index = mark_complete - 1
            
            # remove completed todo from list 
            print(f'{todos.pop(completed_index)} is marked completed')

        case 'exit':
            break
        case _:
            print('This is an unknown command.')

print('See you soon.')

