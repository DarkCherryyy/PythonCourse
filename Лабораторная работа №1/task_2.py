weight = 1.44 * 1024 * 1024
count_of_lists = 100
count_of_strok = 50
count_of_symbols = 25
weight_of_symbol = 4

weight_of_book = weight_of_symbol * count_of_symbols * count_of_strok * count_of_lists

print("Количество книг, помещающихся на дискету:", int(weight // weight_of_book))
