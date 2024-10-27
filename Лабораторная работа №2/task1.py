money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0
flag = True

while flag:
    if (spend <= money_capital + salary):
        month += 1
    else:
        flag = False
    money_capital -= spend - salary
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", month)
