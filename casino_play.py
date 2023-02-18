import casino_logic
play = input('Поиграем? Если да введите Y если нет N')
if play == 'Y':
    casino_logic
elif play == 'N':
    print('Тогда в следующий раз')
    exit()
else:
    print('Y или N')