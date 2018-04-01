import account
import val

def main():
    rate = int(input('Введите ставку:'))
    money = int(input('Введите сумму:'))
    period = int(input('Введите период:'))
    result = account.calculate_income(rate,period,money)

    result2 = val.perevod(result)
    print ("Параметры счета:\n", "Сумма",money, "\n", "Ставки", rate, "\n", "Период", period, "\n", "Общая сумма", result, "\n")
if __name__=="__main__":
    main()
