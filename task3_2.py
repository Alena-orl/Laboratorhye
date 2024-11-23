# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
arg = "|"
def find_common_participants(str1, str2, a):
    list1=str1.split(a)
    list2=str2.split(a)
    return list(set(list1)&set(list2))

# TODO Провеьте работу функции с разделителем отличным от запятой

res = find_common_participants(participants_first_group, participants_second_group, arg)

print(res)