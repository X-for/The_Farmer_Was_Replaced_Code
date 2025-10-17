from move_to_xy import move_to
from unlocked_sth import unlock_sth

def plant_item(item):
    if item in [Entities.Carrot, Entities.Pumpkin, Entities.Cactus]:
        if get_ground_type() == Grounds.Grassland:
            till()
        plant(item)
    elif item == Entities.Tree and get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
        plant(Entities.Tree)
    else:
        if get_ground_type() == Grounds.Soil:
            till()
        plant(item)
    if num_items(Items.Fertilizer) >= 1 and use_item(Items.Fertilizer):
        if not can_harvest() and get_entity_type() != None:
            if get_water() <= 0.3 and num_items(Items.Water) >= 2:
                use_item(Items.Water, 2)

def average_item():# 返回较少的变量
    if num_items(Items.Hay) < num_items(Items.Wood):
        return Entities.Grass
    elif num_items(Items.Wood) < num_items(Items.Carrot):
        if (get_pos_x() + get_pos_y()) % 2 == 0:
            return Entities.Tree
        else:
            return Entities.Bush
    elif num_items(Items.Carrot) < num_items(Items.Pumpkin):
        return Entities.Carrot
    elif num_items(Items.Pumpkin) < num_items(Items.Cactus):
        return Entities.Pumpkin
    else:
        return Entities.Cactus

def plant_sth(sth):
    # needs = {
        #    Items.Cactus: [get_cost(Items.Cactus)[Items.Pumpkin]],
            #Items.Pumpkin: [get_cost(Items.Pumpkin)[Items.Carrot]],
            #Items.Carrot: [get_cost(Items.Carrot)[Items.Hay], get_cost(Items.Carrot)[Items.Wood]]
            #}
    if sth == Entities.Cactus:
        if get_cost(sth)[Items.Pumpkin] <= num_items(Items.Pumpkin):
            return Entities.Cactus
        else:
            return plant_sth(Entities.Pumpkin)
    elif sth == Entities.Pumpkin:
        if get_cost(sth)[Items.Carrot] <= num_items(Items.Carrot):
            return Entities.Pumpkin
        else:
            return plant_sth(Entities.Carrot)
    elif sth == Entities.Carrot:
        if get_cost(sth)[Items.Hay] >= num_items(Items.Hay):
            return Entities.Grass
        elif get_cost(sth)[Items.Wood] >= num_items(Items.Wood):
            if (get_pos_x() + get_pos_y()) % 2 == 0:
                return Entities.Bush
            else:
                return Entities.Tree
        else:
            return Entities.Carrot
    elif sth == Entities.Sunflower:
        if get_cost(sth)[Items.Carrot] >= num_items(Items.Carrot):
            return plant_sth(Entities.Carrot)
        else:
            return Entities.Sunflower

def my_harvest():
    if get_entity_type() == Entities.Carrot:
        if can_harvest():
            harvest()
    elif get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == Entities.Grass:
        harvest()
    else:
        if can_harvest():
            harvest()

def plant_everywhere(n):
    for i in range(n):
        for j in range(n):
            if num_items(Items.Power) < 1000:
                if get_entity_type() == Entities.Sunflower:
                    if can_harvest():
                        harvest()
                else:
                    harvest()
                if get_ground_type() == Grounds.Grassland:
                    till()
                plant(plant_sth(Entities.Sunflower))
                # plant_item(average_item())
            elif get_entity_type() == None:
                # plant_item(plant_sth(Entities.Cactus))
                plant_item(average_item())
            elif can_harvest() or get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == Entities.Grass:
                my_harvest()
                if num_items(Items.Weird_Substance) >= num_unlocked(Unlocks.Mazes) * 1000 and False:
                    plant(Entities.Bush)
                    use_item(Items.Weird_Substance, num_unlocked(Unlocks.Mazes))
                    harvest()
                # plant_item(plant_sth(Entities.Cactus))
                plant_item(average_item())
            nd_water = (1 - get_water()) / 0.25
            if num_items(Items.Water) > nd_water:
                use_item(Items.Water, nd_water)
            else:
                use_item(Items.Water, num_items(Items.Water))
            move(North)
        move(East)
        
def main_func():
    n = get_world_size()
    change_hat(Hats.Straw_Hat)
    move_to(n // 2, 0)
    
    while True:
        plant_everywhere(n)
        unlock_sth()

    