def count_letters(str_):
    str_ = str_.lower()
    dictionary_letters = {}

    for letter in str_:
        if letter.isalpha():
            if letter not in dictionary_letters:
                dictionary_letters[letter] = 1
            else:
                dictionary_letters[letter] += 1
    return dictionary_letters


def calculate_frequency(dict_):
    sum_count = 0
    dictionary_frequency = {}

    for count in dict_.values():
        sum_count += count

    for key, value in dict_.items():
        dictionary_frequency[key] = value / sum_count
    return dictionary_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

dictionary_count_letters = count_letters(main_str)
frequency_letters = calculate_frequency(dictionary_count_letters)
for key, value in frequency_letters.items():
    print(f'{key}: {value:.2f}')
