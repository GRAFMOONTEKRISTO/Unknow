import mouse
import time


def move_mouse(x, y):
    mouse.move(x, y, absolute=True, duration=0.2)


start_x = 100
start_y = 100

coordinates = [
    (411, 745),
    (133, 238),
    (699, 655),
    (702, 518),
    (646, 517),
    (700, 364)

]

mouse.move(start_x, start_y, absolute=True, duration=0.2)
time.sleep(2)
for coord in coordinates:
    move_mouse(coord[0], coord[1])
    time.sleep(2)
    mouse.click('left')
    time.sleep(2)

# print(mouse.get_position())
