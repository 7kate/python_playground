"""
Напишите программу, заполняющую массив n × n следующим образом: на побочной диагонали стоят нули, выше диагонали двойки, ниже единицы.
"""
q=int(input("Введите размеры масива (N): "))
a=[]
for i in range (q):
    b=[]
    for j in range(q,0,-1):
        if i==j-1:
            b+=[0]
        elif i<j:
            b+=[2]
        else:
            b+=[1]
    a+=[b]
for i in range (q):
    print(*a[i],sep="")
