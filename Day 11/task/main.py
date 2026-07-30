import random
import art


# deal cards
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10.10]
    card = random.choice(cards)
    return card


# user choice and computer choice compare
def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# add cards to the user and computer
def compare(u_score, c_score):
    if u_score == c_score:
        return "------ Draw -------"
    elif u_score == 0:
        return "----- Win with Blackjack ------"
    elif c_score == 0:
        return "------ You loose! Opponent has Blackjack ------"
    elif u_score > 21:
        return "------- You lose! -------"
    elif c_score > 21:
        return "------ You win! -------"
    elif u_score > c_score:
        return "------- You win ------"
    else:
        return "------ You lose -------"


# print the intro
def play():
    print(art.logo)
    user_card = []
    user_score = -1
    comp_card = []
    comp_score = -1
    is_game_over = False

    for i in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    while not is_game_over:
        user_score = calculate(user_card)
        comp_score = calculate(comp_card)
        print(f"Your cards: {user_card}\nYour score: {user_score}\n\nComputer's first card: {comp_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_continue = input("Do you want to get another card? \n 'y' for yes 'n' for pass: ")
            if user_continue == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    print(f"Your final hand: {user_card}\nYour final score: {user_score}")
    print(f"Computer final hand: {comp_card}\n Computer's final score: {comp_score}")
    print(compare(user_score, comp_score))

    print


choice1 = input("Do you want to play a round of Blackjack?\npress 'y' for yes, 'n' for no: ")
if choice1 == "y":
    print("\n" * 20)
    play()
