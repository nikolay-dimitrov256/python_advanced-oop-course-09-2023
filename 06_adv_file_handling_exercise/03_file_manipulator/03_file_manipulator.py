import os


def create_file(file_name: str):
    open(file_name, 'w').close()


def add_content(file_name: str, content: str):
    with open(file_name, 'a') as file:
        file.write(content + '\n')


def replace_content(file_name: str, old_string: str, new_string: str):
    try:
        with open(file_name, 'r') as file:
            text = file.read()

    except FileNotFoundError:
        print('An error occurred')
        return

    else:
        text = text.replace(old_string, new_string)
        with open(file_name, 'w') as file:
            file.write(text)


def delete_file(file_name: str):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print('An error occurred')


def base_function():
    while True:
        command, *params = input().split('-')
        if command == 'End':
            break

        if command == 'Create':
            file_name = params[0]
            create_file(file_name)

        elif command == 'Add':
            file_name = params[0]
            content = params[1]
            add_content(file_name, content)

        elif command == 'Replace':
            file_name = params[0]
            old_string = params[1]
            new_string = params[2]
            replace_content(file_name, old_string, new_string)

        elif command == 'Delete':
            file_name = params[0]
            delete_file(file_name)


base_function()
