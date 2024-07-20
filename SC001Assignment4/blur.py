"""
File: blur.py
Name: Shawn Chan
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    Blur the image.
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x + 1, y)
                pixel3 = img.get_pixel(x, y + 1)
                pixel4 = img.get_pixel(x + 1, y + 1)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) / 4
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) / 4
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) / 4
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == img.width - 1 and y == 0:
                # Get pixel at the top-right corner of the image.
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x, y + 1)
                pixel4 = img.get_pixel(x - 1, y + 1)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) / 4
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) / 4
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) / 4
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == 0 and y == img.height - 1:
                # Get pixel at the bottom-left corner of the image
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel4 = img.get_pixel(x + 1, y)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) / 4
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) / 4
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) / 4
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == img.width - 1 and y == img.height - 1:
                # Get pixel at the bottom-right corner of the image
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x - 1, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) / 4
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) / 4
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) / 4
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif 0 < x < img.width - 1 and y == 0:
                # Get top edge's pixels (without two corners)
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x - 1, y + 1)
                pixel4 = img.get_pixel(x, y + 1)
                pixel5 = img.get_pixel(x + 1, y + 1)
                pixel6 = img.get_pixel(x + 1, y)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) / 6
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.red + pixel6.red) / 6
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.red + pixel6.blue) / 6
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif 0 < x < img.width - 1 and y == img.height - 1:
                # Get bottom edge's pixels (without two corners)
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x - 1, y - 1)
                pixel4 = img.get_pixel(x, y - 1)
                pixel5 = img.get_pixel(x + 1, y - 1)
                pixel6 = img.get_pixel(x + 1, y)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) / 6
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.red + pixel6.red) / 6
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.red + pixel6.blue) / 6
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == 0 and 0 < y < img.height - 1:
                # Get left edge's pixels (without two corners)
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel4 = img.get_pixel(x + 1, y)
                pixel5 = img.get_pixel(x + 1, y + 1)
                pixel6 = img.get_pixel(x, y + 1)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) / 6
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.red + pixel6.red) / 6
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.red + pixel6.blue) / 6
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == img.width - 1 and 0 < y < img.height - 1:
                # Get right edge's pixels (without two corners)
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x - 1, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel5 = img.get_pixel(x - 1, y + 1)
                pixel6 = img.get_pixel(x, y + 1)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) / 6
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.red + pixel6.red) / 6
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.red + pixel6.blue) / 6
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            else:
                # Inner pixels.
                pass
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x + 1, y)
                pixel4 = img.get_pixel(x - 1, y - 1)
                pixel5 = img.get_pixel(x, y - 1)
                pixel6 = img.get_pixel(x + 1,y - 1)
                pixel7 = img.get_pixel(x - 1, y + 1)
                pixel8 = img.get_pixel(x, y + 1)
                pixel9 = img.get_pixel(x + 1, y + 1)
                avg_red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red + pixel7.red +
                           pixel8.red + pixel9.red) / 9
                avg_green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green +
                             pixel7.green + pixel8.green + pixel9.green) / 9
                avg_blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue +
                            pixel7.blue + pixel8.blue + pixel9.blue) / 9
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

    return new_img


if __name__ == '__main__':
    main()
