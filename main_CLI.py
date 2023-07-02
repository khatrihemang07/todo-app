import functions
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print('It is',now)
while True:
    user_action=input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    if user_action.startswith('add'):
        todo=user_action[4:]
        todos=functions.get_todos()
        todos.append(todo+'\n')
        functions.write_todos(todos)
    elif user_action.startswith('show'):
        todos=functions.get_todos()
        for index, item in enumerate(todos):
            item=item.strip()
            print(f"{index+1}. {item}")
    elif user_action.startswith('edit'):
        number=int(user_action[5:])
        number=number-1
        todos=functions.get_todos()
        new_todo=input("Enter new todo: ")+'\n'
        todos[number]=new_todo
        functions.write_todos(todos)
    elif user_action.startswith('complete'):
        number=int(user_action[9:])
        todos=functions.get_todos()
        index=number-1
        todo_to_remove=todos.pop(index).strip()
        functions.write_todos(todos)
        print(f'Todo "{todo_to_remove}" was removed from the list')
    elif user_action.startswith('exit'):
        break
    else:
        print("Incorrect command. Please re-enter. Thank you")

