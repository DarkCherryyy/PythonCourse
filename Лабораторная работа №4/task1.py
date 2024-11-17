import json


def task() -> float:
    sum_ = 0

    with open('input.json', 'r') as file:
        data = json.load(file)

    for i in range(len(data)):
        sum_ += data[i].get("score") * data[i].get("weight")

    return round(sum_, 3)


print(task())
