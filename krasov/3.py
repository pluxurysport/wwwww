def search(string):
    substring = input("Введите подстроку: ")
    number = string.find(substring)
    if number < 0:
        print("Данная подстрока в строку не входит!")
    else:
        print("Первое вхождение подстроки начинается с", number+1,"символа")
#функция разбивает строку на отдельные слова и отсортировывает их в алфавитном порядке
def sort(string):
    string = string.lower()
    words  = string.split(' ') #разбиение строки по пробелу
    words.sort()
    print("Слова в алфавитном порядке: ")
    for word in words:
      print(word)
#функция подсчета вхождения символов в строку(выводит только символы с ненулевым значением, общее число различных символов)
def symbol(string):
    dictionary = {}
    for letter in string:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                print('Ошибка!\n')
    d = 0
    p = ''
    for key in dictionary.keys():
        p += str(key) + ' : ' + str(dictionary[key]) + ',  '
        if d == 5:
            d = 0
            print(p, '\n')
            p = ''
        else:
            d += 1
    print('Количество различных символов в строке: ', len(dictionary))
def main():
    line = input("Введите строку: ")
    print(line)
    print('\n')
    symbol(line)
    line = line.strip() #удаление пробелов
    search(line)
    sort(line)
if __name__ == '__main__':
    main()
