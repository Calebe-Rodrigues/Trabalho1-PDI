from src.convertions import *


def negativeRBG(img):
    pixel_map = img.load()

    width = img.width
    height = img.height

    for i in range(width):
        for j in range(height):

            r, g, b = pixel_map[i, j]

            new_r = 255 - r
            new_g = 255 - g
            new_b = 255 - b

            pixel_map[i, j] = (new_r, new_g, new_b)


def negativeV(img):
    pixel_map = img.load()

    width = img.width
    height = img.height

    for i in range(width):
        for j in range(height):

            r, g, b = pixel_map[i, j]
            h, s, v = RGBtoHSB(r, g, b)

            inv = 1.0 - v

            new_r, new_g, new_b = HSBtoRGB(h, s, inv)

            pixel_map[i, j] = (new_r, new_g, new_b)
