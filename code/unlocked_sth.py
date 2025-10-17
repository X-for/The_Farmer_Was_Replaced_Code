its = [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin, Items.Cactus, Items.Gold, Items.Bone]
ulcs = [Unlocks.Grass, Unlocks.Expand, Unlocks.Carrots, 
        # Unlocks.Watering, 
        Unlocks.Cactus, Unlocks.Trees, 
        # Unlocks.Fertilizer, 
        # Unlocks.Polyculture, 
        Unlocks.Dinosaurs,]

def unlock_sth():
    for ulc in ulcs:
        can_unlocked = True
        costs = get_cost(ulc)
        for key in costs:
            if num_items(key) < costs[key]:
                can_unlocked = False
                break
        if can_unlocked:
            unlock(ulc)
            print('unlocked', ulc)