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
    set_world_size(5)
    for i in range(1):
        if num_drones() > 1:
            continue
        init()
        DFS()
solve()
