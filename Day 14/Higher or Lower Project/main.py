import random
from game_data import data
from art import logo, vs
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def account():
    person = random.choice(data)
    return {
        'text': f"{person['name']}, {person['description']} from {person['country']}.",
                'followers': person['follower_count'],
                'raw' : person
    }




def compare(a,b):

    print(f"Compare A: {a['text']}")
    print (vs)
    print(f"Against B: {b['text']}")

def result(foll_a, foll_b, choice):
    if (choice == "a" and foll_a > foll_b) or (choice == "b" and foll_b > foll_a) :
        return True
    else:

        return False


print(logo)
choice_a = account()
score = 0
while True:
    choice_b = account()
    while choice_a['raw'] == choice_b['raw']:
        choice_b = account()
    a_followers = choice_a['followers']
    b_followers = choice_b['followers']
    compare(choice_a,choice_b)
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = result(a_followers, b_followers, user_choice)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
        choice_a = choice_b
    else:
        final_score = score
        print(f"Sorry, that's wrong. Final score: {final_score}")
        break