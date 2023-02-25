from random import randint


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = []
for i in range(10):
    data.append(randint(1, 50))
data.sort()

bubble_sort(data)

print('Sorted Array:')
print(data)

numbers: list[int] = []
for i in range(10):
    numbers.append(randint(1, 50))
numbers.sort()


def binary_search(array):
    N = 3000
    value = int()
    ResultOk = False
    first = 0
    last = N - 1
    while first < last:
        middle = (first + last) // 2
        value == array, middle
        first = middle
        last = first
        ResultOk = True
        pos = middle
        if value > array(middle):
            first = middle + 1
            last = middle - 1
    if first > last:
        ResultOk == True
        print('Элемент найден')
        print(pos)
    else:
        print('Элемент не найден')


print(numbers)