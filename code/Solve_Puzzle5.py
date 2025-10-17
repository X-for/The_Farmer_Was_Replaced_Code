dir = [North, East, South, West]
set_world_size(5)
n = get_world_size()


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
    change_hat(hats[(get_pos_x() * n + get_pos_y()) % len(hats)])
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
    for i in range(n):
        visited.append([])
        for j in range(n):
            visited[i].append(False)
    plant(Entities.Bush)
    substance = n * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

def solve():

    for i in range(1):
        if num_drones() > 1:
            continue
        init()
        DFS()


solve()




