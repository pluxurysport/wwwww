print("0 в качестве знака операции завершит работу программы")
while True:
    s = input("Выберите операцию (xor,or,and,not): ")
    if s == '0': break
    if s in ('xor', 'or', 'and', 'not'):
        if s == 'xor':
           x = int(input("x="))
           y = int(input("y="))
           print("%.2f" % (x ^ y))
        elif s == 'or':
            x = int(input("x="))
            y = int(input("y="))
            print("%.2f" % (x | y))
        elif s == 'and':
            x = int(input("x="))
            y = int(input("y="))
            print("%.2f" % (x & y))
        elif s == 'not':
            x = int(input("x="))
            if x != 0:
                print("%.2f" % (~x))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
