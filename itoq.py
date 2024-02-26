def filter_strings(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result

# Пример использования:

# Ввод массива с клавиатуры
input_array = input("Введите элементы массива через запятую: ").split(", ")

# Или задание массива на старте выполнения алгоритма
# input_array = ["Hello", "2", "world", ":-)"]

filtered_array = filter_strings(input_array)
print("Исходный массив:", input_array)
print("Отфильтрованный массив:", filtered_array)