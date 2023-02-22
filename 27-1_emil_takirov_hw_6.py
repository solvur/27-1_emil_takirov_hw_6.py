import re

while True:
    options = int(input('Меню с опциями: \n'
                'Введите 1 что-бы считать имена и фамилии, \n'
                'Введите 2 что-бы считать все емайлы, \n'
                'Введите 3 что-бы считать названия файлов, \n'
                'Введите 5 что-бы выйти\n'
                'Поле для ввода --->'))

    if options == 1:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            full_names = re.findall(r"[A-Z][a-z-]+\s+[a-zA-Z][a-zA-Z- ']*", text)
            with open('names.txt', 'w', encoding='utf-8') as file:
                file.write(str(', ').join(full_names))
    elif options == 2:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            emails = re.findall(r'[a-z|\d]+@[a-z|\d-]+\.[a-z]{2,3}\.?[a-z]*', text)
            with open('emails.txt', 'w', encoding='utf-8') as file:
                file.write(str(', ').join(emails))
    elif options == 3:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            files = re.findall(r'[A-Z][a-zA-Z]*\.[a-z\d]{3,4}', text)
            with open('files.txt', 'w', encoding='utf-8') as file:
                file.write(str(', ').join(files))
    elif options == 4:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            colors = re.findall(r'#[\d|a-z]{6}', text)
            with open('colors.txt', 'w', encoding='utf-8') as file:
                file.write(str(', ').join(colors))
    elif options == 5:
        break

