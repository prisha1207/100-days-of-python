import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors] #ordered list with index 0,1,2


print("0 for Rock\t1 for Paper\t2 for Scissors")
user_choice = int(input("Enter your choice: "))
if user_choice in range(0,3):
    print("Your choice: \n",game[user_choice])

comp_choice=random.randint(0,2)
print("Computers Choice: ")
print(game[comp_choice])

if user_choice>=3 or comp_choice<0:
    print("Invalid Choice")
elif user_choice==0 and comp_choice==2:
    print("You win!")
elif user_choice==0 and comp_choice==1:
    print("You lose!")
elif comp_choice>user_choice:
    print("You lose!")
elif user_choice>comp_choice:
    print("You win!")
elif comp_choice==user_choice:
    print("It's a draw!")
else:
    print("You typed an invalid number! You lose! ")



