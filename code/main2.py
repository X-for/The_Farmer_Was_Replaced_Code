from move_to_xy import move_to


hats = [
    Hats.Gray_Hat, 
    Hats.Purple_Hat, 
    Hats.Green_Hat, 
    Hats.Brown_Hat, 
    Hats.Gold_Hat, 
    Hats.Straw_Hat,
    Hats.Sunflower_Hat,
    Hats.Cactus_Hat,
    Hats.Tree_Hat,
    Hats.Wizard_Hat,
    Hats.Cactus_Hat,
    Hats.Golden_Cactus_Hat,
    Hats.Golden_Pumpkin_Hat,
    Hats.Golden_Tree_Hat,
    Hats.The_Farmers_Remains,
    Hats.Top_Hat,
    Hats.Traffic_Cone,
    Hats.Traffic_Cone_Stack,
    ]



def plant_item(item):
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
    if False and num_items(Items.Fertilizer) >= 16 and use_item(Items.Fertilizer):
        if not can_harvest() and get_entity_type() != None:
            if get_water() <= 0.3 and num_items(Items.Water) >= 2:
                use_item(Items.Water, 2)

def average_item():# 返回较少的变量
    ets = [Entities.Grass, Entities.Tree, Entities.Bush, Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
    if num_items(Items.Hay) < num_items(Items.Wood) / 10:
        return Entities.Grass
    elif num_items(Items.Wood) / 10 < num_items(Items.Carrot):
        if (get_pos_x() + get_pos_y()) % 2 == 0:
            return Entities.Tree
        else:
            return Entities.Bush
    elif num_items(Items.Carrot) < num_items(Items.Pumpkin):
        return Entities.Carrot
    elif num_items(Items.Pumpkin) < num_items(Items.Cactus):
        return Entities.Pumpkin
    else:
        if (get_pos_x() + get_pos_y()) % 2 == 0:
            return Entities.Cactus
        else:
            return ets[random() * (len(ets) - 1) // 1]

def plant_sth(sth):
    # needs = {
        #    Items.Cactus: [get_cost(Items.Cactus)[Items.Pumpkin]],
            #Items.Pumpkin: [get_cost(Items.Pumpkin)[Items.Carrot]],
            #Items.Carrot: [get_cost(Items.Carrot)[Items.Hay], get_cost(Items.Carrot)[Items.Wood]]
            #}
    n = get_world_size()

    if sth == Entities.Cactus:
        if get_cost(sth)[Items.Pumpkin] * n <= num_items(Items.Pumpkin) and (get_pos_x() + get_pos_y()) % 2 == 0:
            return Entities.Cactus
        else:
            return plant_sth(Entities.Pumpkin)
    elif sth == Entities.Pumpkin:
        if get_cost(sth)[Items.Carrot] * n <= num_items(Items.Carrot):
            return Entities.Pumpkin
        else:
            return plant_sth(Entities.Carrot)
    elif sth == Entities.Carrot:
        if get_cost(sth)[Items.Hay] * n >= num_items(Items.Hay):
            return Entities.Grass
        elif get_cost(sth)[Items.Wood] * n >= num_items(Items.Wood):
            if (get_pos_x() + get_pos_y()) % 2 == 0:
                return Entities.Bush
            else:
                return Entities.Tree
        else:
            return Entities.Carrot
    elif sth == Entities.Sunflower:
        if get_cost(sth)[Items.Carrot] * n >= num_items(Items.Carrot):
            return plant_sth(Entities.Carrot)
        else:
            return Entities.Sunflower
    elif sth == Entities.Tree or sth == Entities.Bush:
        if (get_pos_x() + get_pos_y()) % 2 == 0:
            return Entities.Tree
        else:
            return Entities.Bush
            
def my_harvest():
    if get_entity_type() == Entities.Carrot:
        if can_harvest():
            harvest()
    elif get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == Entities.Grass:
        harvest()
    else:
        if can_harvest():
            harvest()
            
def col_func():
    goal = Entities.Cactus
    change_hat(hats[get_pos_x() % len(hats)])
    while True:
        if num_items(Items.Power) < 200:
            if get_entity_type() == Entities.Sunflower:
                if can_harvest():
                    harvest()
            else:
                harvest()
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(plant_sth(Entities.Sunflower))
        elif get_entity_type() == None:
            # plant_item(plant_sth(goal))
            plant_item(average_item())
        elif can_harvest() or get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == Entities.Grass:
            my_harvest()
            if num_items(Items.Weird_Substance) >= num_unlocked(Unlocks.Mazes) * 1000 and False:
                plant(Entities.Bush)
                use_item(Items.Weird_Substance, num_unlocked(Unlocks.Mazes))
                harvest()
            # plant_item(plant_sth(goal))
            plant_item(average_item())
        if get_water() <= 0.5 and num_items(Items.Water) >= 64:
            use_item(Items.Water, 2)
        elif get_water() <= 0.75 and num_items(Items.Water) >= 32:
            use_item(Items.Water, 1)
        move(North)

def main_func():
    move_to(0, 0)
    n = get_world_size()
    for _ in range(n):
        if not spawn_drone(col_func):
            col_func()
        move(East)
        
        
main_func()