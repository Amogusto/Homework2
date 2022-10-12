el = 0
list_in = []
while True:
    el = input("Введите элемент")
    if el == "end":
        break
    list_in.append(el)
list1 = list_in[::2]
list2 = list_in[1::2]
i = 0
j = 0
for pos in range(0, len(list_in) - 1, 2):
    list_in[pos] = list2[i]
    i += 1
for pos in range(1, len(list_in), 2):
    list_in[pos] = list1[j]
    j += 1
for el in list_in:
    print(el)
