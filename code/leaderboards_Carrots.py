from move_to_xy import move_to
from till_to_Soil import till_to_soil_func

def goal():
    if num_items(Items.Carrot) >= 2000000000:
        return False
    else:
        return True

def plant_item(item):
    if get_entity_type() == Entities.Carrot and not can_harvest():
        return 
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

def get_more(x, y):
    n = get_world_size()
    for i in [-1, 1]:
        for j in range(5):
            move_to((x + j) % n , (y + 4 * i - j * i) % n)
            plant_item(Entities.Carrot)

def more_carrot2():
    x, y = get_pos_x(), get_pos_y()
    while goal():
        plant_item(Entities.Carrot)
        if num_items(Items.Fertilizer) >= 1:
            use_item(Items.Fertilizer)
        if get_water() <= 0.75:
            use_item(Items.Water)
        cmp = get_companion()
        if cmp == None:
            harvest()
        else:
            ent, pos = cmp
            move_to(pos[0], pos[1])
            plant_item(ent)
        get_more(x, y)
        move_to(x, y)
        while not can_harvest():
            continue
        harvest()


def mc_func():

    for i in range(4):
        for j in range(4):
            move_to(8 * i + 3, 8 * j + 3)
            if not spawn_drone(more_carrot2):
                more_carrot2()

    for i in range(4):
        for j in range(4):
            move_to(8 * i + 7, 8 * j + 7)
            if not spawn_drone(more_carrot2):
                more_carrot2()

for i in range(get_world_size()):
    if i % 2 == 0:
        plant_item(Entities.Bush)
    else:
        plant_item(Entities.Tree)
    move(North)

till_to_soil_func()
mc_func()