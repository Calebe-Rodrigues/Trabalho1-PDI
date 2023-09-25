from PIL import Image
from src.negative import *
from src.changeHUE import changeHUE
from src.filters import my_filter
import time


if __name__ == '__main__':
    img = Image.open("DancingInWater.jpg")
    img2 = Image.open("testpat.1k.color2.tif")
    img3 = Image.open("Shapes.png")

    start_timer = time.time()

    my_filter(img)
    my_filter(img2)
    my_filter(img3)

    end_timer = time.time()

    print(end_timer-start_timer)

    # changeHUE(img, 90)
    # changeHUE(img2, 90)
    # changeHUE(img3, 90)

    # negativeRBG(img)
    # negativeRBG(img2)
    # negativeRBG(img3)

    # negativeV(img)
    # negativeV(img2)
    # negativeV(img3)

    # img.save("img1.jpg")
    # img2.save("img2.tif")
    # img3.save("img3.png")
