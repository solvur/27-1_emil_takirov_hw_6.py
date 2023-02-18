from random import randint
from decouple import config
capital = config('MY_MONEY', cast=int)
print(f'Ваш капитал {capital}')
while True:
    sum = int(input(f'В вашем кошельке {capital}cом, сколько хотите поставить?'))
    if sum > capital:
        print('У вас нет столько денег')
        break
    roll = int(input('Выберите слот от 1 до 30 '))
    if roll >= 31:
        print('Такого слота нет')
        continue
    elif roll == range (1, 30):
        print(f'Ваша ставка {sum}сом на слот {roll}')

    win_sum = sum * 2
    win_slot = randint(1, 30)
    if win_slot == roll:
        print(f'Поздравляем ваш выйгрыш составил {win_sum}сом!!!')
        win_sum + capital
    elif win_slot != roll:
        print(f'Жаль но вы ничего не выйграли поставив {sum}сом на слот {roll}\n'
            f'Выйгрышный слот был {win_slot}')
        capital -= sum
        if sum  <= 0:
            print('Обидно но вы всё проиграли!')
            print(f'Ваш выйгрыш составил{sum + win_sum}')
            exit()
    print('Хотите ли сыграть ещё раз? если да введите y если нет n')
    question = input()
    if question == 'y':
        play
    elif question == 'n':
        exit()