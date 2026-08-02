# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies #you are calling the global var, and changing its value permanently, in and out the function
    #otherwise, you would have only changed its value inside the function, while outside the function, its value would have remained 1
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


