# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import os
from art import logo
print(logo)
bids = {}

finish = False
def highest_bid(bidding_dict):
    max_bid = 0
    max_bidder = ""
    for key in bidding_dict:
        if bids[key] > max_bid:
            max_bid = bids[key]
            max_bidder = key
    print(f"{max_bidder} has won the auction with a bid of {max_bid}€")

while not finish:
    name = input("What's your name?: ")
    price = int(input("What's your bid?: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? y/n: ")
    os.system('cls')
    if should_continue == "n":
        finish = True
        highest_bid(bids)



