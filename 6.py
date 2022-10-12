dataset = []
datainfo = {"Название":[], "Цена":[], "Количество":[], "ед.":[]}
for i in range(1, 3):
    name = input(f"Введите название товара {i}: ")
    price = input(f'Введите цену товара: {name}: ')
    count = input(f'Введите количество товара: {name}: ')
    meas = input(f'Введите единицы измерения товара: {name}: ')
    dataset.append((i, {"Название": name, "Цена": price, "Количество": count, "ед": meas}))
print(dataset)

for i in range(2):
    datainfo["Название"].append(dataset[i][1]["Название"])
    datainfo["Цена"].append(dataset[i][1]["Цена"])
    datainfo["Количество"].append(dataset[i][1]["Количество"])
    datainfo["ед."].append(dataset[i][1]["ед."])
print(datainfo)