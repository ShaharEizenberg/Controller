from PIL import ImageGrab, Image
import zlib
import pygame
from pygame.locals import *

def equal(image1, image2):
    """

    :param image1: The old image
    :param image2: The new image
    :return: Returns the bounding box of the difference between the two images
    """
    # Load the first image
    image1.load()
    # Load the second image
    image2.load()
    # The coordinates of the start and the end of the difference box
    coordinates = image1._new(image1.im.chop_difference(image2.im)).getbbox()
    # If the size is to close to the size of the screen send the whole screen
    if coordinates != None and coordinates[2] - coordinates[0] > 1200 and coordinates[3] - coordinates[1] > 700:
        coordinates = (0, 0, 1920, 1080)
    # Return the coordinates of the start and the end of the difference box
    print(coordinates)
    return coordinates

def screenShot():
    """

    :return:
    """
    # Takes the first screen shot
    img1 = ImageGrab.grab()
    return img1


def check_events():
    """

    :return: Check if the client close the pygame window
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

def draw(image, coordinates, width_image, height_image, screen):
    """

    :return:
    """
    check_events()
    print("in draw")
    print(type(image))
    print(len(image))
    print(width_image, height_image)
    # Match the image by size and color
    img = pygame.image.frombuffer(image, (width_image, height_image), "RGB")
    print("image")
    # Put the image on the screen
    screen.blit(img, coordinates)
    # Update the screen
    pygame.display.update()
    print("finish drawing")

def paste_on_img(img2, img1, coordinates):
    """

    :param img2: the image to paste
    :param img1: the image to paste on
    :param coordinates: the coordinates of the left top corner to paste on
    :return:
    """
    Image.Image.paste(img2, img1, (coordinates[0], coordinates[1]))