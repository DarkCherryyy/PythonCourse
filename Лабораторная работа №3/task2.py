def find_common_participants(str_1, str_2, spliter=','):
    first_group = set(str_1.split(spliter))
    second_group = str_2.split(spliter)

    common_participants = list(first_group.intersection(second_group))
    common_participants.sort()

    return (common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, spliter='|'))
