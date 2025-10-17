from move_to_xy import move_to

hats = [
    Hats.Gray_Hat, 
    Hats.Purple_Hat, 
    Hats.Green_Hat, 
    Hats.Brown_Hat, 
    Hats.Gold_Hat, 
    Hats.Straw_Hat,
    Hats.Sunflower_Hat,
    Hats.Cactus_Hat,
    Hats.Tree_Hat,
    Hats.Wizard_Hat,
    Hats.Cactus_Hat,
    Hats.Golden_Cactus_Hat,
    Hats.Golden_Pumpkin_Hat,
    Hats.Golden_Tree_Hat,
    Hats.The_Farmers_Remains,
    Hats.Top_Hat,
    Hats.Traffic_Cone,
    Hats.Traffic_Cone_Stack,
    ]


n = get_world_size()
def flip_24h():
    change_hat(hats[(get_pos_x()) % len(hats)])
    now = get_time()
    while get_time() - now <= 24 * 60 * 60:
        do_a_flip()


x, y = 0, 0
dx, dy = 1, 1
for i in range(max_drones()):
    move_to(x, y)
    x += dx
    y += dy
    if x >= n or y >= n:
        x, y = 0, n - 1
    if not spawn_drone(flip_24h):
        flip_24h()