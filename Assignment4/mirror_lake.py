"""
File: mirror_lake.py
Name: Shawn Chan
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    Produce a mirrored image flipped vertically
    """
    original_mt = SimpleImage(filename)
    b_img = SimpleImage.blank(original_mt.width, original_mt.height * 2)
    for x in range(original_mt.width):
        for y in range(original_mt.height):
            img_pixel = original_mt.get_pixel(x, y)
            b_img_pixel = b_img.get_pixel(x, y)
            b_img_pixel2 = b_img.get_pixel(x, b_img.height-1-y)

            b_img_pixel.red = img_pixel.red
            b_img_pixel.green = img_pixel.green
            b_img_pixel.blue = img_pixel.blue

            b_img_pixel2.red = img_pixel.red
            b_img_pixel2.green = img_pixel.green
            b_img_pixel2.blue = img_pixel.blue
    return b_img


def main():
    """
    TODO:
    """
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
