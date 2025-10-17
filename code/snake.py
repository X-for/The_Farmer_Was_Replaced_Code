from move_to_xy import move_to
from till_to_Soil import till_to_soil_func

set_world_size(14)
size = get_world_size()

def snake(n):
    eatn = 0
    move(North)
    for i in range(n):
        for j in range(n - 2):
            if i % 2 == 0:
                move(North)
            else:
                move(South)
        move(East)
    move(South)
    while move(West):
        continue
    if can_move(North) or can_move(South) or can_move(East) or can_move(West):
        pass
    else:
        change_hat(Hats.Straw_Hat)
        change_hat(Hats.Dinosaur_Hat)


till_to_soil_func()
change_hat(Hats.Straw_Hat)
move_to(0, 0)
change_hat(Hats.Dinosaur_Hat)
n = size - size % 2
while True:
    snake(n)