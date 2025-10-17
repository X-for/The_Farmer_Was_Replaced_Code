def get_Weird_Substance():
    return

def get_maze(n):
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, num_unlocked(Unlocks.Mazes) * n)

def gm_main(n):
    while True:
        if num_items(Items.Weird_Substance) <= num_unlocked(Unlocks.Mazes) * n * 100 :
            plant(Entities.Grass)
            use_item(Items.Fertilizer)
            while not can_harvest():
                do_a_flip()
            harvest()
        else:
            pass
gm_main(get_world_size())

