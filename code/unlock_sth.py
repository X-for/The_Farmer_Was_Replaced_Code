ulkeds = [
    Unlocks.Grass,
    Unlocks.Speed,
    Unlocks.Plant,
    Unlocks.Debug,
    Unlocks.Expand,
    Unlocks.Carrots,
    Unlocks.Trees,
    Unlocks.Watering,
    Unlocks.Sunflowers,
    Unlocks.Pumpkins,
    Unlocks.Cactus,
    Unlocks.Fertilizer,
    Unlocks.Mazes,
    Unlocks.Megafarm,
    Unlocks.Timing,
    Unlocks.Simulation,
    Unlocks.Dinosaurs,
    Unlocks.Leaderboard,
]

def ulk(x):
    for k in x:
        if num_items(k) < x[k]:
            return False
    return True

def all_locked(tlc=None):
    for x in ulkeds[:len(ulkeds) - 1]:
        if num_unlocked(x) == 0:
            return False
    return True

def unlock_sth():
    for x in ulkeds:
        if not get_cost(x):
            continue
        else:
            if not ulk(get_cost(x)):
                continue
            else:
                unlock(x)
                return x