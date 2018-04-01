def calculate_income(rate,period,money):
    if money <= 0:
        return 0
    for i in range (1, period+1):
        money  = round (money + period*money*(rate/100/12),2)
        return money
def main ():
    rate = 10
    money = 10000
    period = 12
    result = calculate_income(rate, period, money)
    print ("Параметры счета:\n", "Сумма",money, "\n", "Ставки", rate, "\n", "Период", period, "\n", "Общая сумма", result, "\n")
if __name__=="__main__":
    main()
