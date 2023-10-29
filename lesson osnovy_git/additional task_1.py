# Дополнительное задание 1

# Напишите функцию, которая принимает на вход список строк и возвращает список строк,
# в которых первая и последняя буквы совпадают. Если список пустой, верните пустой список.

# Примеры входных данных:

# ['hello', 'world', 'apple', 'pear', 'banana', 'pop']
# ['', 'madam', 'racecar', 'noon', 'level', '']
# []

# Примеры выходных данных:

# ['pop']
# ['', 'madam', 'racecar', 'noon', 'level', '']
# []


def check_the_lines(lines: list[str]) -> list[str]:
    """Возвращает список подстрок,
    в которых первая и последняя буквы совпадают."""
    new_list = []
    for line in lines:
        if line == "":
            new_list.append(line)
        else:
            if line[0] == line[-1]:
                new_list.append(line)

    return new_list


# Проверка работы функции:
data_list = ["", "madam", "racecar", "noon", "level", ""]
print(check_the_lines(data_list))
