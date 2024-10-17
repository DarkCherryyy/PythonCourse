numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

number_none, sum = 0, 0
for i in range(0, len(numbers)):
    if (numbers[i] == None):
        number_none = i
    else:
        sum += numbers[i]
numbers[number_none] = sum/len(numbers)
print("Измененный список:", numbers)
