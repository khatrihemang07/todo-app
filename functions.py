FILEPATH='todos.txt'
def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as fl:
        todos_local=fl.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath,'w') as fl:
        fl.writelines(todos_arg)

if __name__=='__main__':
    print("hello")
