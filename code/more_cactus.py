from move_to_xy import move_to
import func_tools
from till_to_Soil import till_to_soil_func

m = 7

# 修正方向字典
dir = {(1, 0): East, (-1, 0): West, (0, 1): North, (0, -1): South}

def sort_cactus():
    change_hat(Hats.Green_Hat)
    start_x, start_y = get_pos_x(), get_pos_y()
    # 对列进行冒泡排序
    for col in range(m):
        for i in range(m - 1):
            for j in range(m - 1 - i):
                move_to(start_x + col, start_y + j)
                current_val = measure()
                next_val = measure(North)
                    
                if current_val > next_val:
                    # 交换相邻元素
                    swap(North)

    # 对行进行冒泡排序
    for row in range(m):
        for i in range(m - 1):
            for j in range(m - 1 - i):
                move_to(start_x + j, start_y + row)
                current_val = measure()
                next_val = measure(East)
                    
                if current_val > next_val:
                    # 交换相邻元素
                    swap(East)

def sort_ColCactus(l=4):
    # 对列进行冒泡排序
    start_x, start_y = get_pos_x(), get_pos_y()
    for col in range(l):
        for i in range(m - 1):
            for j in range(m - 1 - i):
                move_to(start_x + col, start_y + j)
                current_val = measure()
                next_val = measure(North)
                    
                if current_val > next_val:
                    # 交换相邻元素
                    swap(North)

def sort_RowCactus(l=4):
    # 对行进行冒泡排序
    start_x, start_y = get_pos_x(), get_pos_y()
    for row in range(l):
        for i in range(m - 1):
            for j in range(m - 1 - i):
                move_to(start_x + j, start_y + row)
                current_val = measure()
                next_val = measure(East)
                    
                if current_val > next_val:
                    # 交换相邻元素
                    swap(East)

def plant_Cactus(l = 4):
    # 种植仙人掌
    for i in range(l):
        plant(Entities.Cactus)
        for j in range(m - 1):
            if i % 2 == 0:
                move(North)
            else:
                move(South)
            plant(Entities.Cactus)
        move(East)


def more_cactus2():
    n = get_world_size()
    start_x, start_y = get_pos_x(), get_pos_y()
    # print(start_x, start_y)
    while True:
        # 种植仙人掌
        move_to(start_x + 3, start_y)
        sp = spawn_drone(plant_Cactus)
        move_to(start_x, start_y)
        plant_Cactus(3)
        wait_for(sp)
        
        move_to(start_x + 3, start_y)
        sp = spawn_drone(sort_ColCactus)
        move_to(start_x, start_y)
        sort_ColCactus(3)
        move_to(start_x, start_y + 3)
        wait_for(sp)


        sp = spawn_drone(sort_RowCactus)
        move_to(start_x, start_y)
        sort_RowCactus(3)
        move_to(start_x, start_y)
        wait_for(sp)

        # sp = spawn_drone(sort_cactus)

        harvest()

def mp2_func():
    n = get_world_size()
    for i in range(n // (m + 1)):
        for j in range(n // (m + 1)):
            move_to(i * (m + 1), j * (m + 1))
            if not spawn_drone(more_cactus2):
                more_cactus2()

till_to_soil_func()
mp2_func()