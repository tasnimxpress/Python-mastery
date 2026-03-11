todos = []

while True:
    user_action = input('Type add, show or exit: ')
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
        case 'exit':
            break
        case _:
            print('This is an unknown command.')


print('See you soon.')
