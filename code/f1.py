reach = {}
visited = {}
s = set()
ms_pos_gb = (-1, -1)


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
    nxt = 0
    while len(s) != 100:
        DFS(n)
    ms_pos = ms_pos_gb
    cnt = 0
    while num_items(Items.Weird_Substance) > num_unlocked(Unlocks.Mazes) * n:
        # 获取当前位置
        current_x, current_y = get_pos_x(), get_pos_y()
        current_pos = current_x * n + current_y

        # 使用BFS找到路径
        path = BFS(current_pos, ms_pos, n)

        # 沿着路径移动
        for direction in path:
            move(direction)

        ms_x, ms_y = measure()
        ms_pos = ms_x * n + ms_y
        use_item(Items.Weird_Substance, num_unlocked(Unlocks.Mazes) * get_world_size())
        cnt += 1
        if cnt == 20:
            break


    current_x, current_y = get_pos_x(), get_pos_y()
    current_pos = current_x * n + current_y

    # 使用BFS找到路径
    path = BFS(current_pos, ms_pos, n)

    # 沿着路径移动
    for direction in path:
        move(direction)
    harvest()


def BFS(start_pos, target_pos, n):
    # 初始化访问标记、父节点记录和队列
    visited = {}
    parent = {}

    # 初始化所有位置为未访问
    for i in range(n):
        for j in range(n):
            pos = i * n + j
            visited[pos] = False
            parent[pos] = None

    queue = [start_pos]
    visited[start_pos] = True

    while queue:
        current_pos = queue.pop(0)

        # 如果找到目标位置，重建路径
        if current_pos == target_pos:
            return reconstruct_path(parent, start_pos, target_pos, n)

        # 遍历所有可达的相邻位置
        for next_pos in reach[current_pos]:
            if not visited[next_pos]:
                visited[next_pos] = True
                parent[next_pos] = current_pos
                queue.append(next_pos)

    # 如果没有找到路径，返回空列表
    return []


def reconstruct_path(parent, start, target, n):
    # 从目标位置回溯重建完整路径
    path = []
    current = target

    # 从目标回溯到起点
    while current != start:
        prev = parent[current]
        # 计算移动方向
        direction = get_move_direction(prev, current, n)
        path.append(direction)
        current = prev

    # 反转路径，使其从起点到终点
    return path[::-1]


def get_move_direction(from_pos, to_pos, n):
    # 根据两个位置计算移动方向
    from_x, from_y = from_pos // n, from_pos % n
    to_x, to_y = to_pos // n, to_pos % n

    dx = to_x - from_x
    dy = to_y - from_y

    if dx == 1 and dy == 0:
        return East
    elif dx == -1 and dy == 0:
        return West
    elif dx == 0 and dy == 1:
        return North
    elif dx == 0 and dy == -1:
        return South
    else:
        # 处理意外情况，返回默认方向
        return East


def DFS(n):
    pos = get_pos_x() * n + get_pos_y()
    visited[pos] = True
    s.add(pos)

    # 检查当前实体类型
    entity_type = get_entity_type()
    if entity_type == Entities.Treasure:
        global ms_pos_gb  # 声明为全局变量
        ms_pos_gb = get_pos_x() * n + get_pos_y()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nxt = pos + dx * n + dy
        if 0 <= nxt and nxt < n * n:
            if visited[nxt]:
                continue
            if mv(dx, dy):
                # 确保双向连接
                if nxt not in reach[pos]:
                    reach[pos].append(nxt)
                if pos not in reach[nxt]:
                    reach[nxt].append(pos)
                DFS(n)
                mv(-dx, -dy)


def sp_main():
    n = get_world_size()
    for i in range(n):
        for j in range(n):
            reach[i * n + j] = []
            visited[i * n + j] = False
        plant(Entities.Bush)
        use_item(Items.Weird_Substance, num_unlocked(Unlocks.Mazes) * get_world_size())
    solvePuzzle(n)

sp_main()
    