


# Квач Вячеслав Алексеевич Б9121-10.03.01отзи
import numpy as np

# Эта часть кода создает матрицу
digit = int(input('Введите число больше 2: '))
if digit <= 2:
    print('неверное число')
else:
    pick = [1, -1]
    matrix = np.random.choice(pick, (digit, digit))
    sum1, sum2 = 0, 0
    print(mtx)

    # Эта часть кода складывает и умножает элементы матрицы
    for i in range(digit):
        sum1 += (matrix[i][digit-1]) * (matrix[i][0])
        for j in range(digit-1):
            sum1 += (matrix[i][j] * (matrix[i][j+1]))
    for j in range(digit):
        sum2 += (matrix[digit-1][j]) * (matrix[0][j])
        for i in range(digit-1):
            sum2 += (matrix[i][j] * (matrix[i+1][j]))
    sum = sum1 + sum2

    print(sum)







