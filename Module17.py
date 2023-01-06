def get_sequence_from_user():
    return str(input("Введите последовательность чисел через пробел\n"))


def get_number_from_user():
    return int(input("Введите любое число\n"))


def user_sequence_to_list(sequence):
    try:
        return list(map(int, sequence.strip().split(" ")))
    except:
        print("Неверная последовательность чисел")
        return user_sequence_to_list(get_sequence_from_user())

def sort_user_list(user_list):
    user_list.sort()
    return user_list


def find_index(sorted_user_list, number, start_index):
    if len(sorted_user_list) == 1:
        return start_index

    middle = len(sorted_user_list) // 2

    if sorted_user_list[middle - 1] < number <= sorted_user_list[middle]:
        return start_index + middle - 1

    if number > sorted_user_list[middle]:
        sorted_user_list = sorted_user_list[middle:]
        start_index += middle
    else:
        sorted_user_list = sorted_user_list[:middle]

    return find_index(sorted_user_list, number, start_index)


result = find_index(
    sort_user_list(user_sequence_to_list(get_sequence_from_user())),
    get_number_from_user(),
    0
)

print("Ответ: " + str(result))