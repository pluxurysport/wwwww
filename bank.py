import account

def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))
    dollar = int(input("Введите курс доллара: "))
    result = account.calculate_income(rate, money, period)

    res = (result/dollar)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: ", result, "\n", "Сумма в долларах: ", res)


if __name__ == "__main__":
    main()
