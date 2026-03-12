todos = []

while True:
    user_action = input('Type add, show, edit or exit: ')
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todo = todo.strip().capitalize()
            todos.append(todo)
        case 'show':
            for item in todos:
                serial = todos.index(item) + 1
                print(serial, item)
        case 'edit':
            edit_option = int(input('Number of the todo to edit: '))
            position = edit_option - 1
            existing_todo = todos[position]
            print(existing_todo)

            new_todo = input('Enter the new todo: ')
            todos[position] = new_todo
            print('todos modified')
        case 'exit':
            break
        case _:
            print('This is an unknown command.')


print('See you soon.')
