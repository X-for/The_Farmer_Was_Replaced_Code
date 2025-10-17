from move_to_xy import move_to

def more_carrot():
    n = get_world_size()
    while True:
        for j in range(n):
            if can_harvest():
                harvest()
            if get_water() < 0.5 and num_items(Items.Water) >= 64:
                use_item(Items.Water, 2)
            plant(Entities.Carrot)
            move(North)

def mc_main():
    move_to(0, 0)
    n = get_world_size()
    sds = []
    for _ in range(n):
        sd = spawn_drone(more_carrot)
        if not sd:
            more_carrot()
        move(East)

while True:
    mc_main()