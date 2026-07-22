#the jump game:
move()
turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_ahead():
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    move()
    turn_left()


i = 6
for i in range(0, 5):
    move_ahead()

move()
turn_right()
move()
turn_right()
move()
turn_left()