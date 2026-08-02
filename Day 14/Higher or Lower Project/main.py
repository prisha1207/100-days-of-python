#Higer or Lower

#import things
import random
from art import logo
from art import vs
from game_data import data


#choosen random A and B and then hide the followers part, but display the rest


#Ask and compare, who's higher
def format_data(choice):
    choice_name=choice["name"]
    choice_description= choice["description"]
    choice_country=choice["country"]
    return f"{choice_name} is a {choice_description} from {choice_country}"

#compare the follower count first
#predict and decide the answer is user chooses a or b accordingly
def compare_choice(user_input,choice_a,choice_b,score):
    foll_a=choice_a["follower_count"]
    foll_b=choice_b['follower_count']
    if foll_a>foll_b:
        if user_input=='a':
            score+=1
            print(f"YOU GOT IT RIGHT!\n Your current score is- {score}")
        else:
            print("SORRY YOU LOOSE")
            continue_game=False
            return continue_game

    else:
        if user_input=='b':
            score+=1
            print(f"YOU GOT IT RIGHT! \n Your current score is- {score}")
        else:
            print("SORRY YOU LOOSE")
            continue_game=False
            return continue_game


#actual execution of the game
#score is set to 0, and the user takes input and changes it to lower case, to prevent case-sensitive inputs
def game():
    score=0
    print(logo)
    continue_game=True
    choice_b=random.choice(data)

    while continue_game:
        choice_a=choice_b
        choice_b=random.choice(data)
        #if both the data is same, we change the B person
        if choice_a==choice_b:
            choice_b=random.choice(data)

        #displaying the 2 people
        print(f"Comparing A: ",format_data(choice_a))
        print(vs)
        print(f"Comparing B: ", format_data(choice_b))

        #take input and compare
        u_input=input("Who do you think has a higher following- ").lower()
        compare_choice(u_input, choice_a, choice_b, score)

game()