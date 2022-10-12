my_list = [3,8,8,6,6,9,9,2]
num = int(input("Введите число"))
if num in my_list :
    i = len(my_list)  - 1 - my_list[::-1].index(num)
    my_list.insert(i, num)
else:
    my_list.insert(0, num)
print(my_list)