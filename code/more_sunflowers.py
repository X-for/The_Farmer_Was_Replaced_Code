from move_to_xy import move_to
from till_to_Soil import till_to_soil_func

change_hat(Hats.Straw_Hat)

def sunflowers():
    n = get_world_size()
    for i in range(5):
        for j in range(n):
            if can_harvest():
                harvest()
            plant(Entities.Sunflower)
            use_item(Items.Water)
            move(North)

def sunflowers_main():
    move_to(0, 0)
    n = get_world_size()
    for _ in range(n):
        if not spawn_drone(sunflowers):
            sunflowers()
        move(East)

till_to_soil_func()
while True:
    sunflowers_main()
    