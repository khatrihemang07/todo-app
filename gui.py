import functions
import PySimpleGUI as sg
import time

sg.theme('black')
clock=sg.Text('',key='clock')
label=sg.Text("Type in a To-Do")
input_box=sg.InputText(tooltip="Enter todo",key='todo',size=46)
add_button=sg.Button(image_source='add.png',image_size=(50,50),mouseover_colors='RosyBrown1',key='add')
list_box=sg.Listbox(values=functions.get_todos(),
                    key='todos',
                    enable_events=True,
                    size=(45,10))
edit_button=sg.Button("edit",size=10,key='edit')

complete_button=sg.Button('Complete',key='complete',size=10)
exit_button=sg.Button('Exit',key='exit',size=10)

row2_col=sg.Column([[edit_button],[complete_button]])
window=sg.Window('My To-Do App',
                 layout=[[clock],
                         [label],
                         [input_box,add_button],
                         [list_box,row2_col],
                         [exit_button]],
                 font=('Helvetica',16))

while True:
    event,value=window.read(timeout=10000)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'add':
            todos=functions.get_todos()
            todos.append(value['todo']+'\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=value['todos'][0].strip())
        case 'edit':
            try:
                todo_to_edit=value['todos'][0]
                new_todo=value['todo'].strip()
                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo+'\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=('Helvetica',16))
        case 'complete':
            try:
                todo_to_remove=value['todos'][0]
                todos=functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 16))
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()