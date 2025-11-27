import random
import time

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
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

def blackjack(cards_in_hand):
    return len(cards_in_hand) == 2 and calculate_total(cards_in_hand) == 21


balance = 1000
while balance > 0:
    print(f"Your balance is {balance}")
    start = input("Wanna play a round of blackjack? (yes/no)").lower()
    if start == 'no':
        break
    elif start != 'yes':
        print("Please type yes or no")
        continue

    while True:
        try:
            bet = int(input("What's your bet? "))
        except ValueError:
            print("Please enter a number")
            continue

        if bet <= 0:
            print("Bet must be positive.")
        elif bet > balance:
            print("You can't bet more than your balance.")
        else:
            break


    hand = []
    computer_hand = []

    draw_card()
    draw_card()
    computer_draw_card()
    computer_draw_card()

    your_total = calculate_total(hand)
    computer_total = calculate_total(computer_hand)

    print(f"you have {hand} and your total is {your_total}" )
    print(f"computer has a {computer_hand[0]}")
    if blackjack(hand):
        print(f"computer has {computer_hand}")
        if blackjack(computer_hand):
            print("Push!")
        else:
            print("Blackjack!")
            balance += bet * 1.5

            continue
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

    doubled = False
    while your_total < 21:
        hit = input("What do you want to do? ('H' for Hit/'S' for Stand/'D' for Double down/'B' for Balance)").lower()

        if hit == 'b':
            print(f'Your balance is {balance}')
            continue

        if hit == 'd':
            if len(hand) != 2:
                print("Can only double down on first turn")
                continue
            if bet > balance:
                print("Not enough cash for a double down")
                continue
            balance -= bet
            bet *= 2
            draw_card()
            your_total = calculate_total(hand)
            print(f"you have {hand} and your total is {your_total}")
            doubled = True
            if your_total > 21:
                print("Bust! Computer won")
                continue
            break
        elif hit == 'h':
            draw_card()
            your_total = calculate_total(hand)
            print(f"you have {hand} and your total is {your_total}")
            if your_total > 21:
                print("BUST! Computer won")
                break
        elif hit == 's':
            break
        else:
            print("Invalid input")
    if your_total <= 21:
        print("computers turn!")
        while computer_total < 17:
            print(f"computer has {computer_hand} and a total of {computer_total} ")
            computer_draw_card()
            computer_total = calculate_total(computer_hand)
            print(f"computer drew a {computer_hand[-1]}")
        print(f"Computer has {computer_hand} with total {computer_total}")
        if computer_total > 21:
            print("COMPUTER BUSTED! You win!")
            balance += bet * 2
        elif your_total > computer_total:
            print("You win!")
        elif your_total < computer_total:
            print("Computer won")
        else:
            print("Push")
print(f"Game Over, your balance is {balance}")