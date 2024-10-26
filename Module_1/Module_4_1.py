from Fake_math import divide as d_1
from True_math import divide as d_2

f = float(input('Введите первое число: делимое - '))
s = float(input('Введите второе число: делитель - '))
result_1 = d_1(f, s)
result_2 = d_2(f, s)
print(result_1)
print(result_2)