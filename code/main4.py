from unlock_sth import unlock_sth, all_locked
from till_to_Soil import till_to_soil_func
from leaderboards_Maze import solve

# 全局变量
n = get_world_size()
canPlant = set()

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

unlock_mapping = {
    Unlocks.Plant: Entities.Bush,
    Unlocks.Trees: Entities.Tree,
    Unlocks.Carrots: Entities.Carrot,
    Unlocks.Pumpkins: Entities.Pumpkin,
    Unlocks.Cactus: Entities.Cactus,
    Unlocks.Sunflowers: Entities.Sunflower,
}

def myHarvest():
    # 收获作物，包括处理死南瓜
    if can_harvest():
        harvest()
        return True
    elif get_entity_type() == Entities.Dead_Pumpkin:
        return True
    return False

def myPlant(entity):
    # 种植指定实体，考虑土壤类型和资源
    # 检查是否需要使用水和肥料
    if get_water() < 0.75 and num_items(Items.Water) >= num_drones():
        use_item(Items.Water)
    
    if num_items(Items.Fertilizer) >= num_drones():
        use_item(Items.Fertilizer)
        harvest()
    
    # 处理草地种植
    if entity == Entities.Grass:
        if get_ground_type() == Grounds.Soil:
            till()
            return True
        harvest()
        return False
    
    # 处理灌木和树木种植
    if entity in [Entities.Bush, Entities.Tree]:
        plant(entity)
        return True
    
    # 处理其他作物种植
    current_entity = get_entity_type()
    if current_entity == None or current_entity == Entities.Dead_Pumpkin or current_entity == Entities.Grass:
        soil_required_types = [Entities.Carrot, Entities.Pumpkin, Entities.Cactus, Entities.Sunflower]
        grass_required_types = [Entities.Grass]
        
        if entity in soil_required_types:
            if get_ground_type() == Grounds.Grassland:
                till()
            # 特殊处理仙人掌
            if entity == Entities.Cactus and (get_pos_x() + get_pos_y()) % 2 == 0:
                plant(Entities.Pumpkin)
                return True
        elif entity in grass_required_types:
            if get_ground_type() == Grounds.Soil:
                till()
        
        plant(entity)
        return True
    
    return False

def plant_what(item=None):
    # 决定种植什么作物
    if item == None:
        # 根据资源数量决定种植优先级
        if num_items(Items.Hay) <= num_items(Items.Wood) // 10:
            return Entities.Grass
        
        if num_items(Items.Wood) // 10 <= num_items(Items.Carrot):
            # 根据位置决定种植灌木或树木
            if (get_pos_x() + get_pos_y()) % 2 == 0:
                if Entities.Bush in canPlant:
                    return Entities.Bush
                return Entities.Grass
            else:
                if Entities.Tree in canPlant:
                    return Entities.Tree
                elif Entities.Bush in canPlant:
                    return Entities.Bush
                return Entities.Grass
        
        if num_items(Items.Carrot) <= num_items(Items.Pumpkin):
            if Entities.Carrot in canPlant:
                return plant_what(Entities.Carrot)
            return plant_what(Entities.Bush)
        
        if num_items(Items.Pumpkin) <= num_items(Items.Cactus):
            if Entities.Pumpkin in canPlant:
                return plant_what(Entities.Pumpkin)
            return plant_what(Entities.Carrot)
        
        if Entities.Cactus in canPlant:
            return plant_what(Entities.Cactus)
        return plant_what(Entities.Pumpkin)
    
    else:
        # 处理指定物品的情况
        cost = get_cost(item)
        
        if item == Entities.Grass:
            return Entities.Grass
        
        if item == Entities.Bush:
            if Entities.Bush in canPlant:
                return Entities.Bush
            return plant_what(Entities.Grass)
        
        if item == Entities.Tree:
            if Entities.Tree in canPlant:
                return Entities.Tree
            return plant_what(Entities.Bush)
        
        if item == Entities.Carrot:
            if num_items(Items.Hay) <= cost[Items.Hay]:
                return Entities.Grass
            if num_items(Items.Wood) <= cost[Items.Wood]:
                if Entities.Bush in canPlant:
                    return Entities.Bush
                return Entities.Grass
            if Entities.Carrot in canPlant:
                return Entities.Carrot
            return Entities.Grass
        
        if item == Entities.Pumpkin:
            if num_items(Items.Carrot) <= cost[Items.Carrot]:
                return plant_what(Entities.Carrot)
            return Entities.Pumpkin
        
        if item == Entities.Cactus:
            if num_items(Items.Pumpkin) <= cost[Items.Pumpkin]:
                return plant_what(Entities.Pumpkin)
            return Entities.Cactus
        
        if item == Entities.Sunflower:
            if num_items(Items.Carrot) <= cost[Items.Carrot]:
                return plant_what(Entities.Carrot)
            if Entities.Sunflower in canPlant:
                return Entities.Sunflower
            return plant_what(Entities.Carrot)
    
    # 默认返回值
    return Entities.Grass

def spawn_main():
    # 主要的生成和种植逻辑
    for _ in range(n):
        # 种植向日葵获取能量
        if num_items(Items.Power) < 500 and num_unlocked(Unlocks.Sunflowers) == 1:
            myPlant(plant_what(Entities.Sunflower))
        
        # 收获和种植逻辑
        if myHarvest():
            substance_needed = max(1, 2 ** (num_unlocked(Unlocks.Mazes) - 1))
            
            # 生成更多无人机
            if max_drones() < 25 and num_items(Items.Weird_Substance) >= substance_needed * num_drones():
                if myPlant(plant_what(Entities.Bush)):
                    if get_entity_type() == Entities.Bush and substance_needed >= 1:
                        use_item(Items.Weird_Substance, substance_needed)
                        harvest()
            
            # 常规种植
            myPlant(plant_what())
        
        move(North)

def snake():
    # 蛇形移动遍历地图
    m = get_world_size()
    change_hat(Hats.Dinosaur_Hat)
    
    while True:
        move(North)
        for i in range(m):
            for j in range(m - 2):
                if i % 2 == 0:
                    move(North)
                else:
                    move(South)
            move(East)
        
        move(South)
        while move(West):
            pass
        
        if not measure():
            change_hat(Hats.Straw_Hat)
            break
        
        # 检查是否还能移动
        if not (can_move(North) or can_move(South) or can_move(East) or can_move(West)):
            change_hat(Hats.Straw_Hat)
            break

def snake_run(times):
    # 运行蛇形移动指定次数
    for _ in range(times):
        snake()

def main():
    # 主函数 
    all_locked_flag = False
    
    while True:
        global n
        n = get_world_size()
        
        # 生成无人机
        for _ in range(3):
            for _ in range(max_drones()):
                if not spawn_drone(spawn_main):
                    spawn_main()
                move(East)
        
        # 解锁功能
        unlock_sth()
        
        # 更新可种植的作物
        for unlock, entity in unlock_mapping.items():
            if num_unlocked(unlock) != 0:
                canPlant.add(entity)
        
        # 检查是否全部解锁
        if not all_locked_flag:
            all_locked_flag = all_locked()
        
        # 骨头收集逻辑
        if num_items(Items.Bone) < 2000000 and n % 2 == 0:
            if all_locked_flag and num_items(Items.Cactus) // 2 > get_cost(Entities.Apple)[Items.Cactus] * (n * n) * 3:
                till_to_soil_func()
                snake_run(2)
        
        # 排行榜解锁后处理
        if max_drones() > 25:
            set_world_size(5)
            solve()
            set_world_size(1)
        
        # 检查是否完成
        if num_unlocked(Unlocks.Leaderboard) == 1:
            break

# 启动程序
main()