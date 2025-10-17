from unlock_sth import unlock_sth, all_locked
from till_to_Soil import till_to_soil_func

n = get_world_size()
canPlant = set()
ulks = {
    Unlocks.Plant: Entities.Bush,
    Unlocks.Trees: Entities.Tree,
    Unlocks.Carrots: Entities.Carrot,
    Unlocks.Pumpkins: Entities.Pumpkin,
    Unlocks.Cactus: Entities.Cactus,
    Unlocks.Sunflowers: Entities.Sunflower,
}

def myHarvest():
    if can_harvest():
        harvest()
        return True
    elif get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
        return True
    else:
        return False

dir = [North, East, South, West]

def delay(t):
    now = get_time()
    while get_time() - now <= t:
        continue


def backward(d):
    if d == North:
        return South
    elif d == South:
        return North
    elif d == East:
        return West
    elif d == West:
        return East
    
def waitForTreasure():
    n = get_world_size()
    while True:
        if get_entity_type() == Entities.Treasure:
            nums = num_items(Items.Weird_Substance)
            substance = n * 2**(num_unlocked(Unlocks.Mazes) - 1)
            use_item(Items.Weird_Substance, substance)
            if nums == num_items(Items.Weird_Substance):
                harvest()
        if get_entity_type() not in [Entities.Treasure, Entities.Hedge]:
            return 

def DFS():
    x, y = get_pos_x(), get_pos_y()
    if visited[get_pos_x()][get_pos_y()]:
        return
    spawn_drone(waitForTreasure)
    
    visited[get_pos_x()][get_pos_y()] = True
    for d in dir:
        if can_move(d):
            move(d)
            DFS()
            move(backward(d))


def init():
    global visited
    visited = []
    n = get_world_size()

    for i in range(n):
        visited.append([])
        for j in range(n):
            visited[i].append(False)
    plant(Entities.Bush)
    substance = n * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

def solve():
    if get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1) * 600 <= num_items(Items.Weird_Substance):
        return
    for i in range(1):
        if num_drones() > 1:
            continue
        init()
        DFS()

def myPlant(entity):
    soilMust_type = [Entities.Carrot, Entities.Pumpkin, Entities.Cactus, Entities.Sunflower]
    grassMust_type = [Entities.Grass]
    if get_water() < 0.75 and num_items(Items.Water) >= num_drones():
        use_item(Items.Water)
    if num_items(Items.Fertilizer) >= num_drones():
        use_item(Items.Fertilizer)
        harvest()
    if entity == Entities.Grass:
        if get_ground_type() == Grounds.Soil:
            till()
            return True
        harvest()
    elif entity in [Entities.Bush, Entities.Tree]:
        plant(entity)
        return True
    elif get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == Entities.Grass:
        if entity in soilMust_type:
            if get_ground_type() == Grounds.Grassland:
                till()
            if entity == Entities.Cactus:
                if (get_pos_x() + get_pos_y()) % 2 == 0:
                    plant(Entities.Pumpkin)
                    return True
        elif entity in grassMust_type:
            if get_ground_type() == Grounds.Soil:
                till()
        plant(entity)
        return True
    else:
        return False
    
def plant_what(item=None):
    if item == None:
        # 根据资源数量决定种植优先级
        if num_items(Items.Hay) <= num_items(Items.Wood) // 10:
            return Entities.Grass
        
        elif num_items(Items.Wood) // 10 <= num_items(Items.Carrot):
            # 根据位置决定种植灌木或树木
            if (get_pos_x() + get_pos_y()) % 2 == 0:
                if Entities.Bush in canPlant:
                    return Entities.Bush
                else:
                    return Entities.Grass
            else:
                if Entities.Tree in canPlant:
                    return Entities.Tree
                elif Entities.Bush in canPlant:
                    return Entities.Bush
                else:
                    return Entities.Grass
        
        elif num_items(Items.Carrot) <= num_items(Items.Pumpkin):
            if Entities.Carrot in canPlant:
                return plant_what(Entities.Carrot)
            else:
                return plant_what(Entities.Bush)
        
        elif num_items(Items.Pumpkin) <= num_items(Items.Cactus):
            if Entities.Pumpkin in canPlant:
                return plant_what(Entities.Pumpkin)
            else:
                return plant_what(Entities.Carrot)
        
        else:
            if Entities.Cactus in canPlant:
                return plant_what(Entities.Cactus)
            else:
                return plant_what(Entities.Pumpkin)
    
    else:
        # 处理指定物品的情况
        cost = get_cost(item)
        
        if item == Entities.Grass:
            return Entities.Grass
        
        elif item == Entities.Bush:
            if Entities.Bush in canPlant:
                return Entities.Bush
            else:
                return plant_what(Entities.Grass)
        
        elif item == Entities.Tree:
            if Entities.Tree in canPlant:
                return Entities.Tree
            else:
                return plant_what(Entities.Bush)
        
        elif item == Entities.Carrot:
            if num_items(Items.Hay) <= cost[Items.Hay]:
                return Entities.Grass
            elif num_items(Items.Wood) <= cost[Items.Wood]:
                if Entities.Bush in canPlant:
                    return Entities.Bush
                else:
                    return Entities.Grass
            else:
                if Entities.Carrot in canPlant:
                    return Entities.Carrot
                else:
                    return Entities.Grass
        
        elif item == Entities.Pumpkin:
            if num_items(Items.Carrot) <= cost[Items.Carrot]:
                return plant_what(Entities.Carrot)
            else:
                return Entities.Pumpkin
        
        elif item == Entities.Cactus:
            if num_items(Items.Pumpkin) <= cost[Items.Pumpkin]:
                return plant_what(Entities.Pumpkin)
            else:
                return Entities.Cactus
        
        elif item == Entities.Sunflower:
            if num_items(Items.Carrot) <= cost[Items.Carrot]:
                return plant_what(Entities.Carrot)
            else:
                if Entities.Sunflower in canPlant:
                    return Entities.Sunflower
                else:
                    return plant_what(Entities.Carrot)
    
    # 默认返回值
    return Entities.Grass

def spawn_main():
    for i in range(n):
        if num_items(Items.Power) < 500 and num_unlocked(Unlocks.Sunflowers) == 1:
            myPlant(plant_what(Entities.Sunflower))
        if myHarvest():
            sbt = max(1, 2**(num_unlocked(Unlocks.Mazes) - 1))
            if max_drones() < 25:
                if num_items(Items.Weird_Substance) >= sbt * num_drones():
                    if myPlant(plant_what(Entities.Bush)):
                        if get_entity_type() == Entities.Bush and sbt >= 1:
                            use_item(Items.Weird_Substance, sbt)
                            harvest()
            myPlant(plant_what())
        move(North)

def snake():
    m = get_world_size()
    change_hat(Hats.Dinosaur_Hat)
    while True:
        move(North)
        for i in range(m):
            for j in range(m - 2):
                if i % 2 == 0:
                    move(North)
                else:
                    move(South)
            move(East)
        move(South)
        while move(West):
            continue
        if can_move(North) or can_move(South) or can_move(East) or can_move(West):
            continue
        else:
            change_hat(Hats.Straw_Hat)
            break
def snake_run(t):
    for i in range(t):
        snake()


def main():
    al = False
    while True:
        global n
        n = get_world_size()
        for i in range(5):
            for i in range(max_drones()):
                if not spawn_drone(spawn_main):
                    spawn_main()
                move(East)
        x = unlock_sth()
        for k in ulks:
            if num_unlocked(k) != 0:
                canPlant.add(ulks[k])
        if not al:
            al = all_locked()
        while num_drones() != 1:
            continue
        if num_items(Items.Bone) < 2000000 and n % 2 == 0: 
            if al and num_items(Items.Cactus) // 2 > get_cost(Entities.Apple)[Items.Cactus] * (n * n) * 3:
                till_to_soil_func()
                snake_run(3)
        if num_items(Items.Gold) < 1000000 and max_drones() >= 25:
            if 5 <= n and 25 <= max_drones():
                set_world_size(5)
                solve()
                while num_drones() != 1:
                    continue
                set_world_size(1)
        if num_unlocked(Unlocks.Leaderboard) == 1:
            break
main()