class Hand:
    def __init__(self, name):
        # имя игрока
        self.name = name
        # Изначально рука пустая
        self.cards = []
 
    def add_card(self, card):
        """ Добавляет карту на руку """
        self.cards.append(card)
 
    def get_value(self):
        """ Метод получения числа очков на руке """
        result = 0
        # Количество тузов на руке. 
        aces = 0
        for card in self.cards:
            result += card.card_value()
            # Если на руке есть туз - увеличиваем количество тузов
            if card.get_rank() == "A":
                aces += 1
        # Решаем считать тузы за 1 очко или за 11
        if result + aces * 10 <= 21:
            result += aces * 10
        return result
 
    def __str__(self):
        text = "%s's contains:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nHand value: " + str(self.get_value())
        return text
    
class Deck:
    def __init__(self):
        import random
        # ранги
        ranks = "23456789TJQKA"
        # масти
        suits = "DCHS"
        # генератор списков создающий колоду из 52 карт
        self.cards = [Card(r,s) for r in ranks for s in suits]
        # перетасовываем колоду. Не забудьте импортировать функцию shuffle из модуля random
        shuffle(self.cards)
 
    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()
    
class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
 
    def card_value(self):
        if self.rank in "TJQK":
            # По 10 за десятку, валета, даму и короля
            return 10
        else:
            # Возвращает нужное число очков за любую другую карту
            # Туз изначально дает одно очко.
            return " A23456789".index(self.rank)
 
    def get_rank(self):
        return self.rank
 
    def __str__(self):
        return "%s%s" % (self.rank, self.suit)
    
def new_game():
    # создаем колоду
    d = Deck()
    # задаем "руки" для игрока и дилера
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    # сдаем две карты игроку
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    # сдаем одну карту дилеру
    dealer_hand.add_card(d.deal_card())
    print (dealer_hand)
    print ("="*20)
    print (player_hand)
    # Флаг проверки необходимости продолжать игру
    in_game = True
    # набирать карты игроку имеет смысл только если у него на руке меньше 21 очка
    while player_hand.get_value() < 21:
        ans = raw_input('Hit or stand? (h/s) ')
        if ans == "s":
            print("You stopped")
            break
        else:
            player_hand.add_card(d.deal_card())
            print (player_hand)
            # Если у игрока перебор - дилеру нет смысла набирать карты
            if player_hand.get_value() > 21:
                print ("You lose")
                ans = input('To play anew?')
                if ans =="s":
                    print("Good bye))")
                    exit(0)
                else:
                        new_game()
                in_game = False
    print ("=" * 20)
    if in_game:
        # По правилам дилер обязан набирать карты пока его счет меньше 17
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print (dealer_hand)
            # Если у дилера перебор играть дальше нет смысла - игрок выиграл
            if dealer_hand.get_value() > 21:
                print ("Dealer bust")
                ans = input('To play anew?')
                if ans =="s":
                    print("Good bye))")
                    exit(0)
                else:
                    new_game()
                in_game = False
    if in_game:
        # Ни у кого не было перебора - сравниваем количество очков у игрока и дилера. 
        # В нашей версии если у дилера и игрока равное количество очков - выигрывает казино
        if player_hand.get_value() > dealer_hand.get_value():
            print("You win")
            ans = input('To play anew?(h/s) ')
            if ans == "s":
                print("Good bye))")
                exit(0)
            else:
                new_game()
        else:
            print("Dealer win")
            ans = input('To play anew?(h/s) ')
            if ans == "s":
                print("Good bye))")
                exit(0)
            else:
                new_game()
