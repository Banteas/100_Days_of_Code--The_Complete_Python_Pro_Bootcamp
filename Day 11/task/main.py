import random
from art import logo
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(my_sum, com_sum):
    if my_sum > com_sum:
        print("You win 😁")
    elif com_sum > my_sum:
        print("You lose 😢")
    elif my_sum == 21 and len(my_cards) == 2 and com_sum == 21 and len(com_cards) > 2 :
        print("Your Blackjack won!!!")
    else:
        print("It's a draw")



def calculate_score(card_s):
    score = sum(card_s)
    if score > 21 and 11 in card_s:
        card_s.remove(11)
        card_s.append(1)
        score = sum(card_s)
    return score


def com_result(my_final_score):

    while calculate_score(com_cards) < 17:

        com_cards.append(random.choice(cards))
    com_final_score = calculate_score(com_cards)
    if com_final_score == 21 and len(com_cards) == 2 and my_final_score == 21 and len(my_cards) == 2:
        print("It is a Draw, you both have Blackjacks")
    elif com_final_score == 21 and len(com_cards) == 2:
        print(f"Your final hand: {my_cards}, final score: {my_final_score}")
        print(f"You lost. Com with {com_cards} had a Blackjack")

    elif com_final_score > 21:
        print(f"Your final hand: {my_cards}, final score: {my_final_score}")
        print(f"Com with {com_cards} and sum = {com_final_score}, gone busted!!. You won 😁")


    else:
        print(f"Your final hand: {my_cards}, final score: {my_final_score}")
        print(f"Com's last hand is {com_cards} and the sum is {com_final_score}")
        compare(my_final_score, com_final_score)







def get_card():
    while True:
        want_card = input("Type 'y' to get a another card, type 'n' to pass: ").lower()
        if want_card == "y":
            my_cards.append(random.choice(cards))
            my_final_score = calculate_score(my_cards)

            print(f"Your cards: {my_cards}, current score: {my_final_score}")
            print(f"Computer's first card: {com_cards[0]}")

            if my_final_score > 21: # should add case that I have an Ace
                print(f"Your final hand: {my_cards}, final score: {my_final_score}")
                print(f"Computer's final hand: {com_cards}, final score {com_cards_sum}")
                print("You went over. You lose 😢")
                break

        else:
            com_result(calculate_score(my_cards))
            break



should_continue = True
while should_continue:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards = [random.choice(cards), random.choice(cards), ]
    com_cards = [random.choice(cards), ]
    my_cards_sum = calculate_score(my_cards)
    com_cards_sum = sum(com_cards)
    should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if should_continue == "y":
        clear_console()
        print(logo)
        print(f"Your cards: {my_cards}, current score: {my_cards_sum}")
        print(f"Computer's first card: {com_cards}")

        if sum(my_cards) == 21:
            print("You have a Blackjack!!")
            com_result(my_cards_sum)
        else:
            get_card()

    else:
        should_continue = False