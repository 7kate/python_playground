"""
Создать первый кортеж из 10 случайных чисел (от 1 до 10) и второй —
из удвоенных элементов первого ( использовать генератор списков)
"""
from random import randint
a1=tuple(randint(1,10)for i in range (10))
a2=tuple(x**2 for x in a1 )
print("Сгенерируемый кортеж : ",a1)
print("Обработанны кортеж (квадрат кажого элемента) :",a2)
