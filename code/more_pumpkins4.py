from move_to_xy import move_to
from till_to_Soil import till_to_soil_func

m = 7

def make_sure_pumpkins():
    if get_entity_type() == Entities.Dead_Pumpkin or not can_harvest():
        if get_water() <= 0.5:
            use_item(Items.Water, 2)
        plant(Entities.Pumpkin)
        return True
    else:
        return False



def more_pumpkins3():
    n = get_world_size()
    start_x, start_y = get_pos_x(), get_pos_y()
    while True:
        sp = spawn_drone(make_sure_pumpkins_func)
        for i in range(m):
            plant(Entities.Pumpkin)
            for j in range(m - 1):
                if i % 2 == 0:
                    move(North)
                else:
                    move(South)
                plant(Entities.Pumpkin)
            move(East)
        move_to(start_x, start_y)
        wait_for(sp)
        harvest()


def make_sure_pumpkins_func():
    now = get_time()
    while get_time() - now < 1:
        continue
    ddPumpPos = []
    for i in range(m):
        if make_sure_pumpkins():
            ddPumpPos.append((get_pos_x(), get_pos_y()))
        for j in range(m - 1):
            if i % 2 == 0:
                move(North)
            else:
                move(South)
            if make_sure_pumpkins():
                ddPumpPos.append((get_pos_x(), get_pos_y()))  
        move(East)
    i = 0
    while i < len(ddPumpPos):
        move_to(ddPumpPos[i][0], ddPumpPos[i][1])
        if make_sure_pumpkins():
            ddPumpPos.append((get_pos_x(), get_pos_y()))
        i += 1

def mp2_func():
    till_to_soil_func()
    n = get_world_size()
    for i in range(n // (m + 1)):
        for j in range(n // (m + 1)):
            move_to(i * (m + 1), j * (m + 1))
            if not spawn_drone(more_pumpkins3):
                more_pumpkins3()


mp2_func()
