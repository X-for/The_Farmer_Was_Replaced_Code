from move_to_xy import move_to
from till_to_Grassland import till_to_grass_func

def plant_item(item):
    if get_entity_type() != None:
        harvest()
    if item == Entities.Carrot:
        cost = get_cost(Entities.Carrot)
        if num_items(Items.Hay) < cost[Items.Hay]:
            plant_item(Entities.Grass)
            return
        elif num_items(Items.Wood) < cost[Items.Wood]:
            plant_item(Entities.Bush)
            return 
        elif get_ground_type() == Grounds.Grassland:
            till()
            plant(item)
    else:
        if get_ground_type() == Grounds.Soil:
            till()
        plant(item)

def goal():
    if num_items(Items.Hay) >= 2000000000:
        return False
    return True

def more_grass2():
    x, y = get_pos_x(), get_pos_y()
    while goal():
        if get_water() <= 0.75:
            use_item(Items.Water)
        cmp = get_companion()
        if cmp == None:
            harvest()
        else:
            ent, pos = cmp
            move_to(pos[0], pos[1])
            plant_item(ent)
        move_to(x, y)
        harvest()

def mg_func():
    till_to_grass_func()
    for i in range(4):
        for j in range(4):
            move_to(8 * i + 3, 8 * j + 3)
            if not spawn_drone(more_grass2):
                more_grass2()

    for i in range(4):
        for j in range(4):
            move_to(8 * i + 7, 8 * j + 7)
            if not spawn_drone(more_grass2):
                more_grass2()

mg_func()