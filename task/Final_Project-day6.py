#https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Maze&url=%2Fworlds%2Ftutorial_en%2Fmaze1.json
#Today i learnt new skills and i made Reeborg get to the end of the maze in every single sittuation possible. Bellow is the code that i made. 

def right():
    turn_left()
    turn_left()
    turn_left()

if wall_in_front() and wall_on_right() and is_facing_north():
    turn_left()
else:
    right()

while front_is_clear():
    move()
if wall_in_front():
    turn_left()
    if front_is_clear():
        move()  
while at_goal() == 0:
    if right_is_clear():
        right()
        move()
    elif wall_on_right() and front_is_clear():
        move()
    elif right_is_clear() and front_is_clear():
        move()
    else:
        turn_left()
