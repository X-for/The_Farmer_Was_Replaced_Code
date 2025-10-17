visited = {}


def mv(dx, dy):
    if dx == 1 and dy == 0:
        return move(East)
    elif dx == -1 and dy == 0:
        return move(West)
    elif dx == 0 and dy == 1:
        return move(North)
    elif dx == 0 and dy == -1:
        return move(South)
    else:
        return False


def solvePuzzle(n):
    cnt = 1
    for i in range(cnt):
        init()
        DFS(n)
        if i == cnt - 1 or num_items(Items.Weird_Substance) < n * 2 ** (num_unlocked(Unlocks.Mazes) - 1):
            break
        use_item(Items.Weird_Substance, n * 2 ** (num_unlocked(Unlocks.Mazes) - 1))
        quick_print('time ', i + 1)
    harvest()

def DFS(n):
    pos = get_pos_x() * n + get_pos_y()
    visited[pos] = True
    if get_entity_type() == Entities.Treasure:
        return True

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nxt = pos + dx * n + dy
        if 0 <= nxt and nxt < n * n:
            if visited[nxt]:
                continue
            if mv(dx, dy):
                if DFS(n):
                    return True
                mv(-dx, -dy)
    return False

def init():
    n = get_world_size()
    for i in range(n):
        for j in range(n):
            visited[i * n + j] = False

def sp_main():
    n = get_world_size()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, n * 2 ** (num_unlocked(Unlocks.Mazes) - 1))
    solvePuzzle(n)


t = 1
substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
while substance <= num_items(Items.Weird_Substance) and t > 0:
    visited = {}
    sp_main()
    t -= 1
    