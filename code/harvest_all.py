from move_to_xy import move_to

def harvest_all(n):
    for j in range(n):
        if can_harvest():
            harvest()
        if get_ground_type() == Grounds.Soil:
            till()
        move(North)

def harvest_main():
    i = 1
    while i > 0:
        change_hat(Hats.Straw_Hat)
        harvest_all(get_world_size())
        i -= 1