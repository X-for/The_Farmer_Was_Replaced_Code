from move_to_xy import move_to


move_to(16, 16)
till()
for i in range(-1, 2):
    for j in range(-1, 2):
        move_to(16 + i, 16 + j)
        till()
move_to(16, 16)