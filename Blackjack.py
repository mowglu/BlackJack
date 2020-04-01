import random


# Defining a class that has no specific attribute. It accepts all the cards from the deck(s) as a list.
# It can randomly generate a card that cannot be generated again (using info from list).
class Card():

    def __init__(self):
        pass

    # a function to randomly generate number values that will be used to get information on cards
    def randomcard(self, all_cards):
        # random card index, random card, and popping that random card out of the deck
        randcardind = all_cards.index(all_cards[random.randint(1, len(all_cards) - 1)])
        randcard = all_cards[randcardind]
        all_cards.pop(randcardind)
        return randcard, all_cards


# A class that holds the deck(s) of cards. Attribute is number of decks. It has a function to populate the cards into a list.
class Deck():

    def __init__(self, num=1):
        self.num = num
        pass

    def populate(self):
        deck_list = [None] * (self.num * 52 + 1)
        deck_list[0] = '$$'
        num = 1
        while num <= self.num:
            for index in range(1, self.num * 52 + 1):
                if index % 13 == 0:
                    card_value = 13
                else:
                    card_value = index % 13
                if index >= (num - 1) * 52 + 1 and index <= (num - 1) * 52 + 13:
                    suit, value, deck_num = ('Hearts', card_value, num)
                    deck_list[index] = (suit, value, deck_num)
                elif index >= (num - 1) * 52 + 14 and index <= (num - 1) * 52 + 26:
                    suit, value, deck_num = ('Diamonds', card_value, num)
                    deck_list[index] = (suit, value, deck_num)
                elif index >= (num - 1) * 52 + 27 and index <= (num - 1) * 52 + 39:
                    suit, value, deck_num = ('Spades', card_value, num)
                    deck_list[index] = (suit, value, deck_num)
                else:
                    suit, value, deck_num = ('Clubs', card_value, num)
                    deck_list[index] = (suit, value, deck_num)
                if index % 52 == 0:
                    num += 1
        return deck_list


# A class that holds name and balance as attributes. It has functions that can add money to and withdraw money from an account.
class Account():

    def __init__(self, name='Unknown', balance=100):
        self.name = name
        self.balance = balance
        print("\nHi {}, this is your account!\nCURRENT BALANCE is ${}".format(self.name, self.balance))

    def withdraw_money(self, money):
        while True:
            if money <= self.balance:
                print("You have withdrawn ${} from your balance".format(money))
                self.balance -= money
                break
            else:
                print("Your withdrawal has exceeded your balance. Please withdraw amount upto ${}".format(
                    self.balance))
                while True:
                    try:
                        money = int(input("Try again\n"))
                        break
                    except:
                        print("You need to type a number value!")
        return self.balance

    def add_money(self, money):
        print("You have added ${} to your balance".format(money))
        self.balance += money
        return self.balance


def cardvisual(suit, value):
    '''
    DOCSTRING: This is a function to create the visual INSIDE a card. Involves using a lot of dictionary items
    input: suit and value
    output: the visual as a list, or dictionary, or something!
    '''
    if suit == 'Hearts':
        visualsuit = '\u2665'
    elif suit == 'Diamonds':
        visualsuit = '\u2666'
    elif suit == 'Spades':
        visualsuit = '\u2660'
    else:
        visualsuit = '\u2663'

    # defining a dictionary that holds the representation of each value from 1-13
    dict1 = {1: [' ' * 11, ' ' * 5 + visualsuit + ' ' * 5, ' ' * 4 + visualsuit + ' ' + visualsuit + ' ' * 4,
                 ' ' * 3 + visualsuit * 5 + ' ' * 3, '  ' + visualsuit + ' ' * 5 + visualsuit + '  ',
                 ' ' + visualsuit + ' ' * 7 + visualsuit + ' ', ' ' * 11],
             2: [' ' * 11, '  ' + visualsuit * 7 + '  ', ' ' * 8 + visualsuit + '  ', '  ' + visualsuit * 7 + '  ',
                 '  ' + visualsuit + ' ' * 8, '  ' + visualsuit * 7 + '  ', ' ' * 11],
             3: [' ' * 11, '  ' + visualsuit * 7 + '  ', ' ' * 8 + visualsuit + '  ', '  ' + visualsuit * 7 + '  ',
                 ' ' * 8 + visualsuit + '  ', '  ' + visualsuit * 7 + '  ', ' ' * 11],
             4: [' ' * 11, '  ' + visualsuit + ' ' * 5 + visualsuit + '  ',
                 '  ' + visualsuit + ' ' * 5 + visualsuit + '  ', '  ' + visualsuit * 7 + '  ',
                 ' ' * 8 + visualsuit + '  ', ' ' * 8 + visualsuit + '  ', ' ' * 11],
             5: [' ' * 11, '  ' + visualsuit * 7 + '  ', '  ' + visualsuit + ' ' * 8, '  ' + visualsuit * 7 + '  ',
                 ' ' * 8 + visualsuit + '  ', '  ' + visualsuit * 7 + '  ', ' ' * 11],
             6: [' ' * 11, '  ' + visualsuit * 7 + '  ', '  ' + visualsuit + ' ' * 8, '  ' + visualsuit * 7 + '  ',
                 '  ' + visualsuit + ' ' * 5 + visualsuit + '  ', '  ' + visualsuit * 7 + '  ', ' ' * 11],
             7: [' ' * 11, '  ' + visualsuit * 7 + '  ', ' ' * 8 + visualsuit + '  ', ' ' * 8 + visualsuit + '  ',
                 ' ' * 8 + visualsuit + '  ', ' ' * 8 + visualsuit + '  ', ' ' * 11],
             8: [' ' * 11, '  ' + visualsuit * 7 + '  ', '  ' + visualsuit + ' ' * 5 + visualsuit + '  ',
                 '  ' + visualsuit * 7 + '  ', '  ' + visualsuit + ' ' * 5 + visualsuit + '  ',
                 '  ' + visualsuit * 7 + '  ', ' ' * 11],
             9: [' ' * 11, '  ' + visualsuit * 7 + '  ', '  ' + visualsuit + ' ' * 5 + visualsuit + '  ',
                 '  ' + visualsuit * 7 + '  ', ' ' * 8 + visualsuit + '  ', '  ' + visualsuit * 7 + '  ', ' ' * 11],
             10: [' ' * 11, ' ' + visualsuit + '  ' + visualsuit * 6 + ' ',
                  ' ' + visualsuit + '  ' + visualsuit + ' ' * 4 + visualsuit + ' ',
                  ' ' + visualsuit + '  ' + visualsuit + ' ' * 4 + visualsuit + ' ',
                  ' ' + visualsuit + '  ' + visualsuit + ' ' * 4 + visualsuit + ' ',
                  ' ' + visualsuit + '  ' + visualsuit * 6 + ' ', ' ' * 11],
             11: [' ' * 11, ' ' * 3 + visualsuit * 7 + ' ', ' ' * 6 + visualsuit + ' ' * 4,
                  ' ' * 6 + visualsuit + ' ' * 4, '  ' + visualsuit + ' ' * 3 + visualsuit + ' ' * 4,
                  ' ' * 3 + visualsuit * 4 + ' ' * 4, ' ' * 11],
             12: [' ' * 11, ' ' * 3 + visualsuit * 5 + ' ' * 3, '  ' + visualsuit + ' ' * 5 + visualsuit + '  ',
                  '  ' + visualsuit + ' ' * 5 + visualsuit + '  ',
                  '  ' + visualsuit + ' ' * 3 + visualsuit + ' ' + visualsuit + '  ',
                  ' ' * 3 + visualsuit * 5 + ' ' + visualsuit + ' ', ' ' * 11],
             13: [' ' * 11, ' ' * 3 + visualsuit + ' ' * 4 + visualsuit + '  ',
                  ' ' * 3 + visualsuit + '  ' + visualsuit + ' ' * 4, ' ' * 3 + visualsuit * 2 + ' ' * 6,
                  ' ' * 3 + visualsuit + '  ' + visualsuit + ' ' * 4,
                  ' ' * 3 + visualsuit + ' ' * 4 + visualsuit + '  ', ' ' * 11]
             }
    return dict1[value]


# print("\u2660") - blackspade. 2661 whiteheart 2662 whitediamond 2663 blackclub


def visual(cardsinplay, hits=0, cpuhits=0, passed=0, passedvar=0):
    '''
    DOCSTRING: This is a function meant to visualize the deck and the user's cards along with the CPU's cards
    input: NA
    output: defines the visual of the game. Hitting print formatting included. NEED TO INCLUDE UNHIDING CPU CARD!
    '''
    # top and bottom
    topbot = '  +' + '-----------' + '+'
    # top gap
    topbiggap = '       '
    # hidden layers
    hidden = '  |' + '***********' + '|'
    # big gap used between Deck, Player cards, and CPU cards. Small gap used between the cards themselves
    biggap = '         '
    smallgap = '  '
    # It is the top or bottom line of the card visual
    topbotline = topbot + topbiggap + topbot + topbot + topbot * hits + topbiggap + topbot + topbot + topbot * cpuhits
    # Printing header visual
    print("\n")
    print('      ' + 'Deck' + '\n' +
          '   ' + 'remaining' + '                   ' + '         ' * hits + 'PLAYER CARDS' + '                   ' + '        ' * hits + '       ' * (
                  cpuhits + 1) + 'CPU CARDS' + '\n')
    # printing top line of visual
    print(topbotline)

    # printing the middle lines in a loop, initially
    if hits == 0 and cpuhits == 0:
        for line in range(7):
            if passed == 0 and cpuhits == 0:
                cardnum3 = hidden
            else:
                cardnum3 = '  |' + cardsinplay[3][line] + '|'
            print(hidden + biggap + '|' + cardsinplay[1][line] + '|' + (
                    smallgap + '|' + cardsinplay[2][line] + '|') + topbiggap + cardnum3 + (
                          smallgap + '|' + cardsinplay[4][line] + '|'))
    # IMPORTANT LOGIC FOR VISUALS FOR MIDDLE LINES AFTER HITS
    else:
        for line in range(7):
            if passed == 0 and cpuhits == 0:
                cardnum3 = hidden
            else:
                cardnum3 = '  |' + cardsinplay[3][line] + '|'
            print(hidden + biggap + '|' + cardsinplay[1][line] + '|' + (smallgap + '|' + cardsinplay[2][line] + '|'),
                  end='')

            for i in range(5, hits + 5):
                print(smallgap + '|' + cardsinplay[i][line] + '|', end='')

            if cpuhits == 0:
                print(topbiggap + cardnum3 + smallgap + '|' + cardsinplay[4][line] + '|')

            elif cpuhits != 0:
                print(topbiggap + cardnum3 + smallgap + '|' + cardsinplay[4][line] + '|', end='')
                for j in range(hits + 5, hits + cpuhits + 5):
                    print(smallgap + '|' + cardsinplay[j][line] + '|', end='')
                print('')

    # printing bottom line of visual
    print(topbotline)


def game(playingcards, c2d, card, deck_list, bruuuh, hitsnum, cpuhitsnum=0, passedvar=0):
    '''
    DOCSTRING: Prompts hits or passes from the player. Also makes the CPU play.
    input: cards that were selected randomly
    output: player hits and cpu hits. ALSO MAYBE END RESULT? 3 CONDITIONS IMPLEMENTATION?
    '''
    # Stores the VALUE number of the card, ie face cards are 10! Note that 10 below is an arbitrary large number of possible playing cards.
    # print(passedvar)
    cardnum = [0] * 10
    cardnum[0] = '$$'
    for x in range(1, 5 + hitsnum + cpuhitsnum):
        if playingcards[x][1] in [11, 12, 13]:
            cardnum[x] = 10
        elif playingcards[x][1] != 1:
            cardnum[x] = playingcards[x][1]
        else:
            cardnum[x] = 11

    def continuegame(passedvar=0, hitsnum=0, cpuhitsnum=0):
        if passedvar == 0:
            while True:
                try:
                    answer = input("Enter if you would like to hit or pass? H for hit / Otherwise for pass\n").upper()
                    if answer == 'H':
                        return 4
                    else:
                        return 5
                except:
                    print("Error occurred. Please try again.")
        else:
            if hitsnum == 0 and cpuhitsnum == 0:
                if cardnum[3] + cardnum[4] > cardnum[1] + cardnum[2]:
                    return 2
                else:
                    return 4
            elif hitsnum != 0 and cpuhitsnum == 0:
                sum123 = cardnum[1] + cardnum[2]
                for i in range(5, hitsnum + 5):
                    sum123 += cardnum[i]
                if cardnum[3] + cardnum[4] > sum123:
                    return 2
                else:
                    return 4
            elif hitsnum == 0 and cpuhitsnum != 0:
                while True:
                    sum123 = cardnum[3] + cardnum[4]
                    for i in range(5, cpuhitsnum + 5):
                        sum123 += cardnum[i]

                    if sum123 > 21 and 11 not in [cardnum[3], cardnum[4], cardnum[5:cpuhitsnum + 5]]:
                        return 1
                    elif sum123 > 21:
                        if cardnum[3] == 11:
                            cardnum[3] = 1
                        elif cardnum[4] == 11:
                            cardnum[4] = 1
                        elif cardnum[5] == 11:
                            cardnum[5] = 1
                        else:
                            return 1
                    elif sum123 > cardnum[1] + cardnum[2]:
                        return 2
                    else:
                        return 4
            elif hitsnum != 0 and cpuhitsnum != 0:
                while True:
                    sum123 = cardnum[1] + cardnum[2]
                    for i in range(5, hitsnum + 5):
                        sum123 += cardnum[i]
                    sum456 = cardnum[3] + cardnum[4]
                    for j in range(hitsnum + 5, hitsnum + 5 + cpuhitsnum):
                        sum456 += cardnum[j]

                    if sum456 > 21 and 11 not in [cardnum[3], cardnum[4],
                                                  cardnum[hitsnum + 5:hitsnum + cpuhitsnum + 5]]:
                        return 1
                    elif sum123 > 21:
                        if cardnum[3] == 11:
                            cardnum[3] = 1
                        elif cardnum[4] == 11:
                            cardnum[4] = 1
                        elif cardnum[hitsnum + 5] == 11:
                            cardnum[hitsnum + 5] = 1
                        else:
                            return 1
                    elif sum456 > sum123:
                        return 2
                    else:
                        return 4

    def blackjack(bruuuh, hitsnum, cpuhitsnum, c1, c2, c3, c4, c5, c6, c7=0, c8=0, c9=0):
        '''
        DOCSTRING: a function to get the values and return win/push/lose/hit/pass states. This function has the main logic of BlackJack
        input: the values of cards
        output: win/push/lose/hit/pass states. 1 = win, 2 = lose, 3 = draw, 4 = hit, 5 = pass
        '''
        # initial check with the four cards

        if c1 + c2 == 21:
            print("BLACKJACK! Let's see if the CPU has blackjack, and if not - you win!")
            if c3 + c4 == 21:
                print("BLACKJACK for the CPU!")
                return 3
            else:
                return 1

        # hitting or passing after the first four cards.
        if bruuuh == 0:
            gameval = continuegame()
            return gameval

        else:
            # logic with three cards
            if hitsnum == 1:
                while True:
                    sum = c1 + c2 + c5
                    if sum > 21 and 11 not in [c1, c2, c5]:
                        return 2
                    elif sum > 21:
                        if c1 == 11:
                            c1 = 1
                        elif c2 == 11:
                            c2 = 1
                        elif c5 == 11:
                            c5 = 1
                        else:
                            return 2
                    else:
                        if sum == 21:
                            print(
                                "BLACKJACK! Let's see if the CPU has blackjack. If it has it in less than 3 cards, you lose. If it has it in 3 cards, it's a push (draw). Otherwise, you win!")
                            if c3 + c4 == 21:
                                print("BLACKJACK for the CPU!")
                                return 2
                            elif c3 + c4 + c6 == 21:
                                print("BLACKJACK for the CPU!")
                                return 3
                            else:
                                return 1
                        else:
                            gameval = continuegame(passedvar, hitsnum, cpuhitsnum)
                            return gameval
            if hitsnum == 2:
                while True:
                    sum = c1 + c2 + c5 + c6
                    if sum > 21 and 11 not in [c1, c2, c5, c6]:
                        return 2
                    elif sum > 21:
                        if c1 == 11:
                            c1 = 1
                        elif c2 == 11:
                            c2 = 1
                        elif c5 == 11:
                            c5 = 1
                        elif c6 == 11:
                            c6 = 1
                        else:
                            return 2
                    else:
                        gameval = continuegame(passedvar, hitsnum, cpuhitsnum)
                        return gameval

            gameval = continuegame(passedvar, hitsnum, cpuhitsnum)
            return gameval

    # to perform everything with hitting, including visuals
    def hit(c2d, deck_list, card, hitsnum, cpuhitsnum):
        mycard, deck_list = card.randomcard(deck_list)
        suit = mycard[0]
        value = mycard[1]
        if passedvar == 0:
            hitsnum += 1
        if passedvar != 0:
            cpuhitsnum += 1
        index = 4 + hitsnum + cpuhitsnum
        mycardlist[index] = mycard
        c2d[index] = cardvisual(suit, value)
        visual(c2d, hitsnum, cpuhitsnum)
        return c2d, mycardlist, hitsnum, cpuhitsnum

    # to perform everything with passing, including visuals
    def funcpass(c2d, hitsnum, cpuhits):

        visual(c2d, hitsnum, cpuhits, 1, 0)
        return 1

    gamevalue = blackjack(bruuuh, hitsnum, cpuhitsnum, cardnum[1], cardnum[2], cardnum[3], cardnum[4], cardnum[5],
                          cardnum[6], cardnum[7],
                          cardnum[8], cardnum[9])
    bruuuh += 1
    if gamevalue == 1:
        funcpass(c2d, hitsnum, cpuhitsnum)
        print("Congratulations! You have won this round.")
        account.add_money(betamt * 2)
        return account.balance
    elif gamevalue == 2:
        funcpass(c2d, hitsnum, cpuhitsnum)
        print("Bad luck, you have lost this round.")
        return account.balance
    elif gamevalue == 3:
        funcpass(c2d, hitsnum, cpuhitsnum)
        print("Push! That's a draw.")
        account.add_money(betamt)
        return account.balance
    elif gamevalue == 4:
        c2dupdate, mycardlistupdate, hitsnum, cpuhitsnum = hit(c2d, deck_list, card, hitsnum, cpuhitsnum)
        # print(mycardlistupdate)
        return game(mycardlistupdate, c2dupdate, card, deck_list, bruuuh, hitsnum, cpuhitsnum, passedvar)
    elif gamevalue == 5:
        passedvar = funcpass(c2d, hitsnum, cpuhitsnum)
        # print(mycardlist)
        return game(mycardlist, c2d, card, deck_list, bruuuh, hitsnum, cpuhitsnum, passedvar)


# main function at the end of code
if __name__ == "__main__":

    # intro to the game
    print(
        "\nWelcome to this game of BlackJack! The CPU, and you will both start with two cards. Your job is to hit a higher number total than the CPU before busting (exceeding 21).")
    print(
        "Remember that the cards from 2-10 of any suit have a value corresponding to that number. Jack, Queen, and King each have a value of 10. Ace is a special card that can either be 1 or 11, whichever is beneficial.")
    print("One of the CPU's cards will be hidden, for extra drama. Bet well, and have fun!")
    # deck info and accepting how many decks there are. Suggested value of 1, max value of 3.
    while True:
        try:
            deck_num = int(input(
                "\nPlease enter how many decks of cards you want to play with. Typical BlackJack involves 1 deck of cards.\n"))
            while True:
                if deck_num >= 5:
                    print("Way too many decks, try choosing a number of decks below 5")
                    deck_num = int(input("Try again"))
                    continue
                elif deck_num < 1:
                    print("Need to choose at least 1 deck.")
                    deck_num = int(input("Try again"))
                    continue
                else:
                    break
            break
        except ValueError:
            print("You did not enter an integer. Try again!")
        except:
            print("Some unclassified error. Try entering a number again!")

    # creating object deck of class Deck.
    deck = Deck(deck_num)
    deck_list = deck.populate()
    # print(deck_list)
    # print(len(deck_list))

    # creating object of class Card
    card = Card()

    while True:
        namevar = input("What is your name?\n")
        if type(namevar) == int:
            print("Please type a string of letters for your name.")
        else:
            break

    # Get bet amount as an input
    print("Your balance will be $100 initially.\nINITIAL BALANCE: $100")


    balance = 100
    choice = 'Y'
    while choice == 'Y':
        # create an object of class Account
        account = Account(namevar, balance)
        # Initial bet
        while True:
            try:
                betamt = int(input("Enter your bet amount\n"))
            except:
                print("Please enter a number for your bet amount.")
                continue
            break
        account.withdraw_money(betamt)

        # card info
        print(
            "\nTwo cards will now be drawn for you, and two cards will be drawn for the CPU. Remember, initially one of the CPU's cards is hidden ;)")

        # initialization of list that holds card visual information. It is a 2d list
        c = []
        templist = []
        for i in range(0, 10):
            for j in range(1, 7):
                templist.append('$$')
            c.append(templist)
            templist = []

        check = 1
        mycardlist = [0] * 10
        mycardlist[0] = '$$'
        while check <= 4:
            mycard, deck_list = card.randomcard(deck_list)
            suit = mycard[0]
            value = mycard[1]
            mycardlist[check] = mycard
            # cards being displayed, with an array of cards. First 4 cards.
            c[check] = cardvisual(suit, value)
            check += 1
        # visual of first 4 cards
        visual(c)
        # Starting the game now
        bruuuh = 0
        hitsnum = 0
        cpuhitsnum = 0
        passedvar = 0
        balance = game(mycardlist, c, card, deck_list, bruuuh, hitsnum, cpuhitsnum, passedvar)
        if balance == 0:
            print("Sorry, you're broke! That's the end of the game")
            break
        choice = input("Do you want to play again? Y/N \n").upper()