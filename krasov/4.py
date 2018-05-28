"""
Интерпретатор поддерживает:
Операции: - + * / ^ 
Скобки: ( )
Функции: sin, cos, tg, ctg
"""
#Error0 - неправильно поставили скобки
#Error1 - деление на 0 либо неправильно вычислили ctg
#Интерпретатор на вход принимает строку с операциями, а на выходе возвращает строку ответа, либо кода ошибки.

import math

def block_calculator(expression):
    #Если expression - число, то вернуть его,
    #если нет, то вычислить выражение, содержащее операции одного приоритета
    if check_number(discard_square_brackets(expression)):
        return float(discard_square_brackets(expression))
    else:
        flag_first = True
        left = 0
        available_operations = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}
        if expression.find('^') > 0:
            return exponentiation(expression)
        for i in range(len(expression)):
            if expression[i] == '-' and i != 0 and expression[i - 1] == '[': #Если есть минус как знак числа, то пропустим его
                continue
            elif flag_first and expression[i] in available_operations: # Запись первого числа в result
                result = float(discard_square_brackets(expression[left:i]))
                flag_first = False
                left = i
            elif expression[i] in available_operations: #вычисление операции, если кончился второй операнд
                if expression[left] == '+':
                    result += float(discard_square_brackets(expression[left + 1:i]))
                    left = i
                elif expression[left] == '-':
                    result -= float(discard_square_brackets(expression[left + 1:i]))
                    left = i
                elif expression[left] == '*':
                    result *= float(discard_square_brackets(expression[left + 1:i]))
                    left = i
                elif expression[left] == '/':
                    check_division = float(discard_square_brackets(expression[left + 1:i]))
                    if check_division != 0:
                        result /= check_division
                    else:
                        return 'Error1'
                    left = i
            elif i == len(expression) - 1: #вычисление операции, если она последняя
                if expression[left] == '+':
                    result += float(discard_square_brackets(expression[left + 1:]))
                elif expression[left] == '-':
                    result -= float(discard_square_brackets(expression[left + 1:]))
                elif expression[left] == '*':
                    result *= float(discard_square_brackets(expression[left + 1:]))
                elif expression[left] == '/':
                    check_division = float(discard_square_brackets(expression[left + 1:]))
                    if check_division != 0:
                        result /= check_division
                    else:
                        return 'Error1'
        return result


def exponentiation(expression):
    k = expression.find('^')
    if k > 0:
        return float(discard_square_brackets(expression[:k])) ** exponentiation(expression[k + 1:])
    else:
        return float(discard_square_brackets(expression))


def check_number(expression, flag=False):
    available_numbers = '0123456789.'
    for i in range(len(expression)):
        if expression[i] == '-' and i == 0:
            continue
        elif flag and expression[i] in '[]':
            continue
        elif expression[i] not in available_numbers:
            return False
    return True


def discard_square_brackets(expression):
    if len(expression) > 3 and expression[0] == '[' and expression[-1] == ']':
        return discard_square_brackets(expression[1:-1])
    return expression


def help():
    print("""
    Интерпретатор математических выражений понимает использование следующих символов:
          - + * / ^ ( )
    Можете использовать математические функции:
        sin() cos() tg() ctg() 
    """)

def expression_calculator(expression):
    available_operations = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}

    #Поиск максимального приоритета среди введенных операций
    current = -1
    for i in range(len(expression)):
        if expression[i] in available_operations and current < available_operations[expression[i]]:
            if expression[i] == '-' and expression[i - 1] == '[':
                continue
            else:
                current = available_operations[expression[i]]
    if current == -1:
        return expression


    #Проверка на корректность скобок
    braces = 0
    left_brace = right_brace = -1
    for i in range(len(expression)):
        if expression[i] == '(':
            braces += 1
            left_brace = i
            if i != 0 and expression[i - 1] not in available_operations and expression[i - 1] != '(' and expression[i - 1] not in 'nsg':
                return 'Error0'
        elif expression[i] == ')':
            if braces == 0:
                return 'Error0'
            else:
                braces -= 1
                right_brace = i
            if right_brace - left_brace == 1:
                return 'Error0'
            if i != len(expression) - 1 and expression[i + 1] not in available_operations and expression[i + 1] != ')':
                return 'Error0'
    if braces != 0:
        return 'Error0'

    #Упрощение ф-ций
    while expression.find('sin') != -1 or expression.find('cos') != -1 or expression.find('tg') != -1 or expression.find('ctg') != -1:
        if expression.find('sin') != -1:
            start_of_sin_expression = expression.find('sin') + 4
            sin_expression = expression[expression.find('sin'):]
            braces_sin = 0
            for i in range(len(sin_expression)):
                if sin_expression[i] == '(':
                    braces_sin += 1
                elif sin_expression[i] == ')':
                    if braces_sin == 1:
                        end_of_sin_expression = expression.find('sin') + i
                        break
                    else:
                        braces_sin -= 1
            check = discard_square_brackets(expression_calculator(expression[start_of_sin_expression : end_of_sin_expression]))
            if check == 'Error1':
                return 'Error1'
            else:
                check = round(math.sin(float(check)), 8)
                if check >= 0:
                    if end_of_sin_expression == len(expression) - 1:
                        expression = expression[:start_of_sin_expression - 4] + str(check)
                    else:
                        expression = expression[:start_of_sin_expression - 4] + \
                                     str(check) + \
                                     expression[end_of_sin_expression + 1:]
                else:
                    if end_of_sin_expression == len(expression) - 1:
                        expression = expression[:start_of_sin_expression - 4] + '[' +str(check) + ']'
                    else:
                        expression = expression[:start_of_sin_expression - 4] + \
                                     '[' + str(check) + ']' + \
                                     expression[end_of_sin_expression + 1:]
        elif expression.find('cos') != -1:
            start_of_cos_expression = expression.find('cos') + 4
            cos_expression = expression[expression.find('cos'):]
            braces_cos = 0
            for i in range(len(cos_expression)):
                if cos_expression[i] == '(':
                    braces_cos += 1
                elif cos_expression[i] == ')':
                    if braces_cos == 1:
                        end_of_cos_expression = expression.find('cos') + i
                        break
                    else:
                        braces_cos -= 1
            check = discard_square_brackets(
                expression_calculator(expression[start_of_cos_expression: end_of_cos_expression]))
            if check == 'Error1':
                return 'Error1'
            else:
                check = round(math.cos(float(check)), 8)
                if check >= 0:
                    if end_of_cos_expression == len(expression) - 1:
                        expression = expression[:start_of_cos_expression - 4] + str(check)
                    else:
                        expression = expression[:start_of_cos_expression - 4] + \
                                     str(check) + \
                                     expression[end_of_cos_expression + 1:]
                else:
                    if end_of_cos_expression == len(expression) - 1:
                        expression = expression[:start_of_cos_expression - 4] + '[' + str(check) + ']'
                    else:
                        expression = expression[:start_of_cos_expression - 4] + \
                                     '[' + str(check) + ']' + \
                                     expression[end_of_cos_expression + 1:]

        elif expression.find('tg') != -1:
            start_of_tg_expression = expression.find('tg') + 4
            tg_expression = expression[expression.find('tg'):]
            braces_tg = 0
            for i in range(len(tg_expression)):
                if tg_expression[i] == '(':
                    braces_tg += 1
                elif tg_expression[i] == ')':
                    if braces_tg == 1:
                        end_of_tg_expression = expression.find('tg') + i
                        break
                    else:
                        braces_tg -= 1
            check = discard_square_brackets(expression_calculator(expression[start_of_tg_expression: end_of_tg_expression]))
            if check == 'Error1':
                return 'Error1'
            else:
                check = round(math.tan(float(check)), 8)
                if check >= 0:
                    if end_of_tg_expression == len(expression) - 1:
                        expression = expression[:start_of_tg_expression - 4] + str(check)
                    else:
                        expression = expression[:start_of_tg_expression - 4] + \
                                     str(check) + \
                                     expression[end_of_tg_expression + 1:]
                else:
                    if end_of_tg_expression == len(expression) - 1:
                        expression = expression[:start_of_tg_expression - 4] + '[' + str(check) + ']'
                    else:
                        expression = expression[:start_of_tg_expression - 4] + \
                                     '[' + str(check) + ']' + \
                                     expression[end_of_tg_expression + 1:]

        elif expression.find('ctg') != -1:
            start_of_ctg_expression = expression.find('ctg') + 4
            ctg_expression = expression[expression.find('ctg'):]
            braces_ctg = 0
            for i in range(len(ctg_expression)):
                if ctg_expression[i] == '(':
                    braces_ctg += 1
                elif ctg_expression[i] == ')':
                    if braces_ctg == 1:
                        end_of_ctg_expression = expression.find('ctg') + i
                        break
                    else:
                        braces_ctg -= 1
            check = discard_square_brackets(expression_calculator(expression[start_of_ctg_expression: end_of_ctg_expression]))
            if check == 'Error1':
                return 'Error1'
            else:
                check = round(math.tan(float(check)), 8)
                if check > 0:
                    check = 1 / check
                    if end_of_ctg_expression == len(expression) - 1:
                        expression = expression[:start_of_ctg_expression - 4] + str(check)
                    else:
                        expression = expression[:start_of_ctg_expression - 4] + \
                                     str(check) + \
                                     expression[end_of_ctg_expression + 1:]
                elif check < 0:
                    check = 1 / check
                    if end_of_ctg_expression == len(expression) - 1:
                        expression = expression[:start_of_ctg_expression - 4] + '[' + str(check) + ']'
                    else:
                        expression = expression[:start_of_ctg_expression - 4] + \
                                     '[' + str(check) + ']' + \
                                     expression[end_of_ctg_expression + 1:]
                else:
                    return 'Error1'

    #Отрицательные скобки
    while '(' in expression:
        flag_left_brace = flag_right_brace = True
        left_brace = right_brace = -1
        braces = 0
        for i in range(len(expression)):
            if flag_left_brace and expression[i] == '(':
                braces += 1
                left_brace = i
                flag_left_brace = False
            elif expression[i] == '(' and right_brace == -1:
                braces += 1
            elif expression[i] == ')' and braces != 0:
                braces -= 1
                if flag_right_brace and braces == 0:
                    right_brace = i
                    flag_right_brace = False
        if check_number(expression[left_brace + 1:right_brace]): #Если в скобках  отрицательное число, то меняем круглые скобки на квадратные
            if int(expression[left_brace + 1:right_brace]) < 0:
                expression = expression[:left_brace] + '[' + \
                             expression[left_brace + 1:right_brace] + ']' + \
                             expression[right_brace + 1:]
            else:
                expression = expression[:left_brace] + \
                             expression[left_brace + 1:right_brace] + \
                             expression[right_brace + 1:]
        else:
            check_division = expression_calculator(expression[left_brace + 1:right_brace])
            if check_division == 'Error1':
                return 'Error1'
            else:
                expression = expression[:left_brace] + \
                          check_division + \
                          expression[right_brace + 1:]

   
    #Вычисление блоков операций с максимальным приоритетом с помощью ф-ции block_calculator
    left = 0 #Индекс операции с меньшим приоритетом, чем максимальный, находящейся слева (левая граница блока)
    result_expression = ''
    first_block = True
    for i in range(len(expression)):
        if expression[i] in available_operations and \
                current > available_operations[expression[i]]:
            if expression[i] == '-' and expression[i - 1] == '[':
                continue
            if first_block:
                block_for_record = block_calculator(expression[left:i])
                if block_for_record == 'Error1':
                    return 'Error1'
                elif block_for_record < 0:
                    result_expression = '[' + str(block_for_record) + ']' + expression[i] #запись первого блока
                else:
                    result_expression = str(block_for_record) + expression[i]
                first_block = False
            else:
                block_for_record = block_calculator(expression[left:i])
                if block_for_record == 'Error1':
                    return 'Error1'
                elif block_for_record < 0:
                    result_expression += '[' + str(block_for_record) + ']' + expression[i] #запись первого блока
                else:
                    result_expression += str(block_for_record) + expression[i]
            left = i + 1
        elif left != 0 and i == len(expression) - 1:
            block_for_record = block_calculator(expression[left:])
            if block_for_record == 'Error1':
                return 'Error1'
            elif block_for_record < 0:
                result_expression += '[' + str(block_for_record) + ']'
            else:
                result_expression += str(block_for_record)
    if left == 0:
        block_for_record = block_calculator(discard_square_brackets(expression))
        if block_for_record == 'Error1':
            return 'Error1'
        elif block_for_record < 0:
            result_expression = '[' + str(block_for_record) + ']'
        else:
            result_expression = str(block_for_record)

    #Проверка того, что получен конечный ответ, если нет, то продолжить вычисление
    if check_number(result_expression):
        return result_expression
    else:
        check_division = expression_calculator(result_expression)
        if check_division == 'Error1':
            return 'Error1'
        else:
            return check_division

def check_expression(expression):
    available_symbols = '+-/*^()sct0123456789.'
    available_operations = '+-*/^'
    available_right = '0123456789sct('
    available_left = '0123456789)'
    available_numbers = '0123456789'
    i = 0
    while i < len(expression):
        if expression[i] in available_symbols:
            if expression[i] == 's':
                if expression[i+1:i+4] == 'in(': # Проверка, что 's' часть 'sin('
                    i += 4
                else:
                    return False
            elif expression[i] == 'c':
                if expression[i + 1:i + 4] == 'os(': # Проверка, что 'c' часть 'cos('
                    i += 4
                elif expression[i + 1:i + 4] == 'tg(': # Проверка, что 'c' часть 'ctg('
                    i += 4
                else:
                    return False
            elif expression[i] == 't': # Проверка, что 't' часть 'tg('
                if expression[i+1:i+3] == 'g(':
                    i += 3
                else:
                    return False
            elif expression[i] in available_operations:
                if i == 0 or i == len(expression) - 1 or \
                        expression[i - 1] not in available_left or \
                        expression[i + 1] not in available_right:
                        return False
            elif expression[i] == '.':
                if expression[i - 1] not in available_numbers or expression[i + 1] not in available_numbers:
                    return False
            i += 1
        else:
            return False
    return True

def delete_spaces(expression):
    expression = expression.strip()
    for i in range(len(expression) - 1):
        if expression[i] == ' ':
            expression = expression[:i] + expression[i+1:]
    return expression

def test_expression_calculator():
    print('Testing function: expression_calculator')
    print('Test 1: OK' if expression_calculator('(5+5)') == '10.0' else 'Test 1: Fail')
    print('Test 2: OK' if expression_calculator('5-5(') == 'Error0' else 'Test 2: Fail')
    print('Test 3: OK' if expression_calculator(')5*5') == 'Error0' else 'Test 3: Fail')
    print('Test 4: OK' if expression_calculator('5/5)') == 'Error0' else 'Test 4: Fail')
    print('Test 5: OK' if expression_calculator('(5+5)*5') == '50.0' else 'Test 5: Fail')
    print('Test 6: OK' if float(expression_calculator('5*(5+5)')) == 50 else 'Test 6: Fail')
    print('Test 7: OK' if float(expression_calculator('(5+5)*5/5')) == 10 else 'Test 7: Fail')
    print('Test 8: OK' if float(expression_calculator('(5*5)/(5*5)')) == 1 else 'Test 8: Fail')
    print('Test 9: OK' if float(expression_calculator('(5)')) == 5 else 'Test 9: Fail')
    print('Test 10: OK' if float(expression_calculator('5+(5-((10-5)*5+5))/5')) == 0 else 'Test 10: Fail')

def main():
    print('Для выхода напишите "exit"\nДля получения справки напишите "help"')
    while True:
        expression = input('Введите выражение: ')
        expression = delete_spaces(expression)
        if expression == 'exit':
            print('Exit')
            break
        elif expression == 'test':
            test_expression_calculator()
        elif expression == 'help':
            help()
        else:
            if check_expression(expression):
                result = discard_square_brackets(expression_calculator(expression))
                if result == 'Error0':
                    print('Ошибка! Неправильно поставили скобки.')
                elif result == 'Error1':
                    print('Ошибка! Деление на 0 или неправильно вычислили ctg.')
                else:
                    print('Полученный результат :', result)
                    print('Хотите ещё решить что-то? [y/n]')
                    ans = input('>> ')
                    if ans.lower() != 'y':
                        print('Exit...')
                        break
            else:
                print('Ошибка! Введено неправильное выражение.')
if __name__ == '__main__':
    main()
