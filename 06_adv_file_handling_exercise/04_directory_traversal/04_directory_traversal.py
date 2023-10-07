import os

files = {}
directory_path = f'{input("Select level: ")}/'


def directory_crawl(directory: str, level: int):
    if level < 0:
        return

    for item in os.listdir(directory):
        if item == 'venv' or item == '.idea':
            continue

        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            extension = item.split('.')[-1]

            if extension not in files:
                files[extension] = []
            files[extension].append(item)

        else:
            directory_crawl(os.path.join(directory, item), level - 1)


directory_crawl(directory_path, 1)

with open('report.txt', 'w') as file:
    for ext, value in sorted(files.items()):
        file.write(f'.{ext}\n')

        for file_name in sorted(value):
            file.write(f'- - - {file_name}\n')
