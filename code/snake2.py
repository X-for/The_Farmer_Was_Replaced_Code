from move_to_xy import move_to

n = get_world_size()

def can_move():
    if move(North):
        return True
    elif move(South):
        return True
    elif move(East):
        return True
    elif move(West):
        return True
    else:
        return False


def snake(n):
    cnt = 0
    
    if get_pos_y() == 0:
        move(North)
    for i in range(n):
        for j in range(n - 3):
            if i % 2 == 0:
                move(North)
            else:
                move(South)
        move(East)
    move(North)
    for i in range(n):
        move(West)
    move(South)
    for i in range(n):
        for j in range(n - 3):
            if i % 2 == 0:
                move(South)
            else:
                move(North)
        move(East)
    move(South)
    for i in range(n):
        move(West)
    if not move(North):
        change_hat(Hats.Straw_Hat)
        move_to(0, 0)
        change_hat(Hats.Dinosaur_Hat)

change_hat(Hats.Straw_Hat)
move_to(0, 0)
change_hat(Hats.Dinosaur_Hat)
while True:
    snake(get_world_size())