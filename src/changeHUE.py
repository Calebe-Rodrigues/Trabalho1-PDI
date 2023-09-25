from src.convertions import *


def changeHUE(img, degrees):
    pixel_map = img.load()

    width = img.width
    height = img.height

    for i in range(width):
        for j in range(height):

            r, g, b = pixel_map[i, j]
            h, s, v = RGBtoHSB(r, g, b)

            new_hue = (h + degrees) % 360

            new_r, new_g, new_b = HSBtoRGB(new_hue, s, v)

            pixel_map[i, j] = (new_r, new_g, new_b)
