n = get_world_size()

def move_to(x, y):
    # 计算坐标差值
    dx = x - get_pos_x()
    dy = y - get_pos_y()
    
    # 计算每个方向上的最小步数和方向
    dx_abs = abs(dx)
    dy_abs = abs(dy)
    
    # x方向移动
    if dx_abs <= n - dx_abs:
        # 直接移动更短
        x_steps = dx_abs
        if dx > 0:
            xdir = East
        else:
            xdir = West
    else:
        # 循环移动更短
        x_steps = n - dx_abs
        if dx > 0:
            xdir = West
        else:
            xdir = East
    # y方向移动
    if dy_abs <= n - dy_abs:
        # 直接移动更短
        y_steps = dy_abs
        if dy > 0:
            ydir = North
        else:
            ydir = South
    else:
        # 循环移动更短
        y_steps = n - dy_abs
        if dy > 0:
            ydir = South
        else:
            ydir = North


    for i in range(x_steps):
        move(xdir)
    for j in range(y_steps):
        move(ydir)

def init():
    for i in range(0, 6, 2):
        move_to(i, 0)
        till()
        plant(Entities.Sunflower)
    move_to(0, 0)
