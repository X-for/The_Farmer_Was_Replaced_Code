from move_to_xy import move_to

def more_woods():
    n = get_world_size()
    i = get_pos_x()
    while True:
        for j in range(n):
            if can_harvest():
                harvest()
            if get_water() < 0.5 and num_items(Items.Water) > 64:
                use_item(Items.Water, 2)
            if (i + j) % 2 == 0:
                plant(Entities.Bush)
            else:
                plant(Entities.Tree)
            move(North)

def mc_main():
    move_to(0, 0)
    n = get_world_size()
    sds = []
    for _ in range(n):
        sd = spawn_drone(more_woods)
        if not sd:
            more_woods()
        sds.append(sds)
        move(East)
    
    while num_drones() != 1:
        continue
        
    now = get_time()
    while False and get_time() - now < 60:
        continue
    harvest()

while True:
    mc_main()