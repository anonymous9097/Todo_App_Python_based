def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        return todos


while True:
    user_action = input("Type add, show, edit, complete or exit")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip('\n'), for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("enter a todo : ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
        except ValueError:
            print("Your command is not Valid...")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
        except IndexError:
            print("There is no item with that number...")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid! Please Try Again..")

print("BYE!")
