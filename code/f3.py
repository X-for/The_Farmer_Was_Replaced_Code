from main import main
from harvest_all import harvest_main


def for_all(f):
    def row():
        for _ in range(get_world_size()-1):
            f()
            move(East)
        f()
    t = get_time()
    for _ in range(get_world_size()):
        if not spawn_drone(row):
                row()
        move(North)

for_all(main)