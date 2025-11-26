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

cash = int(input("How much money do you have?"))
while cash > 0:
    bet = int(input('Whats your bet?'))
    cash -= bet
    start = input("Wanna play a round of blackjack? (yes/no)").lower()
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
        print("BLACKJACK!")
        cash += bet + 3 * bet / 2

    while your_total < 21:
        hit = input("Wanna hit? (yes/no)").lower()

        if hit == 'yes':
            draw_card()
            your_total = calculate_total(hand)
            print(f"you have {hand} and your total is {your_total}")
            if your_total == 21:
                print("BLACKJACK")
            elif your_total > 21:
                print("BUST! \nComputer won")
                break
        elif hit == 'no':
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

            if your_total < computer_total <= 21:
                print('computer won')
            else:
                print('you won')
            break