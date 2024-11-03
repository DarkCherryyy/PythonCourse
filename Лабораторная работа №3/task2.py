def find_common_participants(str_1, str_2, spliter=','):
    first_group = str_1.split(spliter)
    second_group = str_2.split(spliter)

    common_participants = []

    for first_participant in first_group:
        if first_participant in second_group:
            common_participants.append(first_participant)
    return (common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, spliter='|'))
