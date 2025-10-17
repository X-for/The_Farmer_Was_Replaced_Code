from move_to_xy import move_to
from till_to_Soil import till_to_soil_func

def plant_item(item):
    if get_entity_type() != None:
        harvest()
    if item in [Entities.Carrot, Entities.Pumpkin, Entities.Cactus, Entities.Sunflower]:
        if get_ground_type() == Grounds.Grassland:
            till()
        plant(item)
    elif item == Entities.Tree and get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
        plant(Entities.Tree)
    else:
        if get_ground_type() == Grounds.Soil:
            till()
        plant(item)
    # if num_items(Items.Fertilizer) >= 16 and use_item(Items.Fertilizer):
    #     if not can_harvest() and get_entity_type() != None:
    #         if get_water() <= 0.3 and num_items(Items.Water) >= 2:
    #             use_item(Items.Water, 2)


def more_carrot3_func():
    cmp = get_companion()
    if cmp == None:
        harvest()
    else:
        ent, pos = cmp
        move_to(pos[0], pos[1])
        plant_item(ent)


def more_carrot3():
    x, y = get_pos_x(), get_pos_y()
    while True:
        # for i in range(2):
        #     for j in range(1, -1, -1):
        #         if can_harvest():
        #             harvest()
        #         move_to(x + i, y + j)
        plant(Entities.Carrot)
        # if num_items(Items.Fertilizer) >= num_drones():
        #     use_item(Items.Fertilizer)
        if get_water() <= 0.75:
            use_item(Items.Water)

        more_carrot3_func()
        move_to(x, y)
        while not can_harvest():
            harvest()


def mc_func():
    # for i in range(4):
    #     for j in range(4):
    #         move_to(i * 8 + 1, j * 8 + 3)
    #         if not spawn_drone(more_carrot3):
    #             more_carrot3()

    # for i in range(4):
    #     for j in range(4):
    #         move_to(i * 8 + 5, j * 8 + 7)
    #         if not spawn_drone(more_carrot3):
    #             more_carrot3()
    for i in range(4):
        for j in range(4):
            move_to(8 * i + 3, 8 * j + 3)
            if not spawn_drone(more_carrot3):
                more_carrot3()

    for i in range(4):
        for j in range(4):
            move_to(8 * i + 7, 8 * j + 7)
            if not spawn_drone(more_carrot3):
                more_carrot3()


till_to_soil_func()
mc_func()