import random
from art import logo

#choose a random number and set it as the answer
def choose_number():
    number=random.randint(0,101)
    #print("I'm thinking of a number between 1 and 100")
    return number

#accept answers and then decide high or low
def take_input(user_input,num):
    if user_input >num:
        print("Too high")
    elif user_input<num:
        print("Too low")
    else:
        print(f"-------You got it! The number was {user_input}!-------")
    return num

#final accepting the difficulty level and executing the loops
def difficulty(lvl):
    num=choose_number()
    if level=='easy':
        i=10
        while i!=0:
            print(f"You have {i} attempts remaining to guess the number.")
            user_input=int(input("Make a guess- "))
            take_input(user_input,num)
            i-=1
            if user_input==num:
                i=0
        if i==0:
            print('If you want to play again, re-run the code!')
            i-=1

        if i==-1:
            print(f"The correct answer was- {num}")
            print("You are out of attempts! Re-run the code to play again!")
        if i==20:
            print('\n')

    elif level=='hard':
        i=5
        while i != 0:
            print(f"You have {i} attempts remaining to guess the number.")
            user_input = int(input("Make a guess- "))
            take_input(user_input,num)
            i -= 1
            if user_input == num:
                i = 0


        if i == -1:
            print(f"The correct answer was- {num}")
            print("You are out of attempts! Re-run the code to play again!")

        if i==0:
            print('If you want to replay, re-run the code!')
            i-=1


    else:
        print("Invalid choice :(")





#start
print(logo)
print("Im thinking of a number between 1 and 100")
level=input("Do you want to play the easy or the hard level?\n Type 'easy' or 'hard' : ")
difficulty(level)

