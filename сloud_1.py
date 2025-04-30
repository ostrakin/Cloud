# Чтение списка чисел от пользователя
nums = list(map(int, input("Введите числа через запятую: ").split(',')))

# Вывод четных чисел
even_numbers = [x for x in nums if x % 2 == 0]
print("Четные числа:", even_numbers)

# Нахождение максимального и минимального числа
max_number = max(nums)
min_number = min(nums)
print("Максимальное число:", max_number)
print("Минимальное число:", min_number)

# Сортировка списка в порядке возрастания (пузырьковая сортировка)
sorted_list = nums.copy()
for i in range(len(sorted_list)):
    for j in range(len(sorted_list) - i - 1):
        if sorted_list[j] > sorted_list[j + 1]:
            sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

print("Отсортированный список:", sorted_list)
