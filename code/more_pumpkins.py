from move_to_xy import move_to


def more_pumpkins():
    n = get_world_size()
    for j in range(n):
        plant(Entities.Pumpkin)
        move(North)
        
    for j in range(n):
        while get_entity_type() == None or not can_harvest():
            if get_water() <= 0.5:
                use_item(Items.Water, 2)
            plant(Entities.Pumpkin)
        move(North)

    
def mp_main():
    move_to(0, 0)
    n = get_world_size()
    sds = []
    for _ in range(n):
        sd = spawn_drone(more_pumpkins)
        if not sd:
            more_pumpkins()
        sds.append(sds)
        move(East)
    
    while num_drones() != 1:
        continue
        
    now = get_time()
    while False and get_time() - now < 60:
        continue
    harvest()

while True:
    mp_main()
    
    
    
        