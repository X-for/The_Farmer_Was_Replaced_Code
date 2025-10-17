from move_to_xy import move_to
from till_to_Soil import till_to_soil_func

n = get_world_size()

def more_cactus2():
    for i in range(n):
        plant(Entities.Cactus)
        move(North)

def sortRow():
    start_x, start_y = get_pos_x(), get_pos_y()
    for i in range(n - 1):
        for j in range(n - 1 - i):
            move_to(start_x + j, start_y)
            current_val = measure()
            next_val = measure(East)
            if current_val > next_val:
                swap(East)

def sortCol():
    start_x, start_y = get_pos_x(), get_pos_y()
    for i in range(n - 1):
        for j in range(n - 1 - i):
            move_to(start_x, start_y + j)
            current_val = measure()
            next_val = measure(North)
            if current_val > next_val:
                swap(North)

def mp2_func():
    n = get_world_size()
    move_to(0, 0)
    for i in range(n):
        if not spawn_drone(more_cactus2):
            more_cactus2()
        move(East)

    move_to(0, 0)
    while num_drones() != 1:
        continue

    for i in range(n):
        if not spawn_drone(sortCol):
            sortCol()
        move(East)
    
    move_to(0, 0)
    while num_drones() != 1:
        continue

    for i in range(n):
        if not spawn_drone(sortRow):
            sortRow()
        move(North)
    while num_drones() != 1:
        continue
    harvest()

def cactus_main():
    till_to_soil_func()
    while True:
        mp2_func()
        
cactus_main()