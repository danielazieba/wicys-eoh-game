import numpy as np
import cv2

desired_map = [
#    "zzzzzzzzzz",
    "fhffffff",
    "ygysyyky",
    "xxxxxxxx",
   # "xxxxxxxxxx",
    "xxxxxxxx"
    ]

def resolve_tile(curr_tile):
    if curr_tile == 's':
        return cv2.imread('stove.png')
    if curr_tile == 'k':
        return cv2.imread('sink2.png')
    if curr_tile == 'h':
        return cv2.imread('upperfridge.png')
    if curr_tile == 'g':
        return cv2.imread('lowerfridge.png')
    if curr_tile == 'f':
        return cv2.imread('purp2.png')
    if curr_tile == 'z':
        return cv2.imread('purple.png')
    if curr_tile == 'y':
        return cv2.imread('cabinet.png')
    if curr_tile == 'x':
        return cv2.imread('kitchen.png')
    return cv2.imread('background.png')

image_height, image_width, image_c = resolve_tile(desired_map[0][0]).shape
final_img = np.zeros((image_height * len(desired_map), image_height * len(desired_map[0]), image_c), np.uint8)
final_img.fill(255)

for row in range(len(desired_map)):
    for col in range(len(desired_map[row])):
        final_img[(row*16):(row*16) + 16, (col*16): (col*16)+16, :] = resolve_tile(desired_map[row][col])

cv2.imwrite('out.png', final_img)
