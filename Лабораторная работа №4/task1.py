import json


def task() -> float:
    sum_ = 0

    with open('input.json', 'r') as file:
        data = json.load(file)

    sum_ = sum([data[i].get("score") * data[i].get("weight") for i in range(len(data))])

    return round(sum_, 3)


print(task())
