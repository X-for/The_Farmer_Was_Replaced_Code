from move_to_xy import move_to

set_world_size(5)
n = get_world_size()
substance = n * 2**(num_unlocked(Unlocks.Mazes) - 1)


def waitForTreasure():
    lst = measure()
    cnt = 0
    while True:
        if get_entity_type() == Entities.Treasure:
            nums = num_items(Items.Weird_Substance)
            use_item(Items.Weird_Substance, substance)
            if nums == num_items(Items.Weird_Substance):
                harvest()
                
def init():
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substance)

def solve():
    for i in range(n):
        for j in range(n):
            move_to(i, j)
            spawn_drone(waitForTreasure)
    while num_items(Items.Gold) <= 9863168:
        if get_entity_type() in [Entities.Treasure, Entities.Hedge]:
            continue
        init()


solve()




