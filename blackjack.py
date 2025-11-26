import random
import time

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,  ]
#deck = cards * 4
hand = []
computer_hand = []
your_total = 0
computer_total = 0


def calculate_total(cards_in_hand):
    total = 0
    aces = 0

    for card in cards_in_hand:
        if card == 'A':
            aces += 1
            total += 11
        else:
            total += card

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total

def draw_card():
    hand.append(random.choice(cards))

def computer_draw_card():
    computer_hand.append(random.choice(cards))

balance = 1000
while balance > 0:
    start = input(f"Your balance is {balance}, Wanna play a round of blackjack? (yes/no)").lower()
    bet = int(input('Whats your bet?'))
    balance -= bet
    if start == 'no':
        break

    hand = []
    computer_hand = []

    draw_card()
    draw_card()
    computer_draw_card()
    computer_draw_card()

    your_total = calculate_total(hand)

    print(f"you have {hand} and your total is {your_total}" )
    print(f"computer has a {computer_hand[0]}")

    if hand == [10, 'A']:
        computer_total = calculate_total(computer_hand)
        if computer_total <= 16:
            print(f"computer has {computer_hand} and a total of {computer_total} ")
            time.sleep(1.7)
            computer_draw_card()
            print(f"computer drew a {computer_hand[-1]}")
        else:
            print(f"computer has {computer_hand} and a total of {computer_total} ")
            if computer_total > 21:
                print("COMPUTER BUSTED")
                balance += bet + 1.5 * bet
            elif computer_total == 21:
                print("That's unfortunate")
                balance += bet
            else:
                print("BLACKJACK!")
                balance += bet + 1.5 * bet

    while your_total < 21:
        hit = input("What do you want to do? ('H' for Hit/'S' for Stand/'D' for Double down/'B' for Balance)").lower()
        if hit == 'b':
            print(f'Your balance is {balance}')
            continue

        if hit == 'd':
            balance -= bet
            draw_card()
            your_total = calculate_total(hand)
            print(f"you have {hand} and your total is {your_total}")
            hit = 'ds'


        if hit == 'h':
            draw_card()
            your_total = calculate_total(hand)
            print(f"you have {hand} and your total is {your_total}")
            if your_total == 21:
                print("BLACKJACK")
            elif your_total > 21:
                print("BUST! \nComputer won")
                break
        elif hit == 's' or 'ds':
            while True:
                computer_total = calculate_total(computer_hand)
                if computer_total <= 16:
                    print(f"computer has {computer_hand} and a total of {computer_total} ")
                    time.sleep(1.7)
                    computer_draw_card()
                    print(f"computer drew a {computer_hand[-1]}")
                else:
                    break
            print(f"computer has {computer_hand} and a total of {computer_total} ")

            if computer_total > 21:
                print("COMPUTER BUSTED")
                if hit == "d":
                    balance += bet*3
                else:
                    balance += bet*2

            if your_total < computer_total <= 21 or your_total > 21:
                print('computer won')
            else:
                print('you won')
            break