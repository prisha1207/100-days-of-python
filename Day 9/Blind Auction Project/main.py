# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import os

def highest_bidder(record):
    higest_bid=0
    winner=""
    for bid in record:
        amount=record[bid]
        if amount>higest_bid:
            higest_bid=amount
            winner=bid

    print(f"The winner is {winner} with the highest bid of ${higest_bid}")


auction={}

auction_count=True
while auction_count:
    name = input("What's your name: ")
    price = float(input("Enter your big price: $"))
    auction[name] = price
    choice = input(print("Do you want to place a new bid? \nY for yes N for no --> "))
    if choice == 'N':
        auction_count = False
        highest_bidder(auction)
    else:
        print("\n"*30)
