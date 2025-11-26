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
    if start == 'no':
        break
    elif start == 'yes':
        while True:
            try:
                bet = int(input("What's your bet? "))
            except ValueError:
                print("Enter a number.")
                continue

            if bet <= 0:
                print("Bet must be positive.")
            elif bet > balance:
                print("You can't bet more than your balance.")
            else:
                break

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

        if len(hand) == 2 and calculate_total(hand) ==21:
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
            elif hit == ('s', 'ds'):
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
                    if hit == "ds":
                        balance += bet*4
                    else:
                        balance += bet*2

                if your_total > 21:
                    print("BUST! Computer won")
                elif computer_total > 21:
                    print("COMPUTER BUSTED, you win")
                elif your_total > computer_total:
                    print("you won")
                elif your_total < computer_total:
                    print("computer won")
                else:
                    print("push")
