from move_to_xy import move_to

m = 7

def make_sure_pumpkins():
    while get_entity_type() == None or not can_harvest():
        if get_water() <= 0.5:
            use_item(Items.Water, 2)
        plant(Entities.Pumpkin)


def more_pumpkins3():
    n = get_world_size()
    start_x, start_y = get_pos_x(), get_pos_y()
    print(start_x, start_y)
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
        move(West)
        
        for i in range(m - 1, m // 2, -1):
            make_sure_pumpkins()
            for j in range(m - 2, -1, -1):
                if i % 2 == 0:
                    move(South)
                else:
                    move(North)
                make_sure_pumpkins()
            move(West)
        move_to(start_x, start_y)
        wait_for(sp)
        harvest()

def make_sure_pumpkins_func():
    for i in range(m):
        make_sure_pumpkins()
        for j in range(m - 1):
            if i % 2 == 0:
                move(North)
            else:
                move(South)
            make_sure_pumpkins()
                
        move(East)

def mp2_func():
    n = get_world_size()
    for i in range(n // (m + 1)):
        for j in range(n // (m + 1)):
            move_to(i * (m + 1), j * (m + 1))
            if not spawn_drone(more_pumpkins3):
                more_pumpkins3()

mp2_func()
