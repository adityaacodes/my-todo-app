FILEPATH = 'todos.txt'

def get_todos(filename=FILEPATH):
    """Reads the text file and returns
    the list of to-do's."""
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filename=FILEPATH):
    """Writes the list of objects in the to-do text file."""
    with open(filename, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(__name__)