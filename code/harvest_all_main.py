from harvest_all import harvest_main
from move_to_xy import move_to

def main_func():
    move_to(0, 0)
    n = get_world_size()
    for _ in range(n):
        if not spawn_drone(harvest_main):
            harvest_main()
        move(East)
    
main_func()