import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, 'text.txt')

try:
    file = open(file_path, 'r')
    print('File found')
    file.close()
except FileNotFoundError:
    print('File not found')
