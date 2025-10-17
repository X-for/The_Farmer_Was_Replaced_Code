from move_to_xy import move_to


def col_func():
    n = get_world_size()
    for j in range(n):
        # if get_entity_type() == Entities.Dead_Pumpkin:
        #     till()
        while not get_entity_type() == Entities.Dead_Pumpkin and not can_harvest() and get_entity_type() != None:
            continue
        harvest()
        if get_ground_type() == Grounds.Grassland:
            till()
        move(North)

def till_to_soil_func():
    n = get_world_size()
    for _ in range(n):
        if not spawn_drone(col_func):
            col_func()
        move(East)
    while num_drones() > 1:
        continue

        