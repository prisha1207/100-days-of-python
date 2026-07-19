print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_amount=bill*(tip/100) #amt of tip to pay
total_bill=bill+tip_amount #amt with the bill
split=total_bill/people #per person
final_amt=round(split,3) #displaying final per person bill up to 2 decimals, rounded

print(f"Each person has to pay: ${final_amt}")


