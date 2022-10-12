sentence = input("Введите предложение:")
words = sentence.split(" ")
i = 1
for word in words:
    print(f'{i}: {word[:9]}')
    i += 1