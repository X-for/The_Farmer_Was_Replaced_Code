from move_to_xy import move_to
from till_to_Grassland import till_to_soil_func


def more_grass():
    n = get_world_size()
    while True:
        for j in range(n):
            harvest()
            move(North)

def mg_func():
    move_to(0, 0)
    n = get_world_size()
    for _ in range(n):
        if not spawn_drone(more_grass):
            more_grass()
        move(East)

move_to(0, 0)
till_to_soil_func()
mg_func()
