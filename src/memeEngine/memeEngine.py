from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime
import random
import os


class MemeEngine:
    def __init__(self, image_path):
        self.img = image_path
        self.width = 0
        self.height = 0
        self.ratio = 1.0
        self.width = 500
        self.height = 500
        self.path_of_saved_images = os.path.abspath(os.getcwd()) + '/files/'

        """ load the image """
        self.img = Image.open(image_path)

        """ setup the image size """
        self.img = self.setup_image_size(self.img)

    def setup_image_size(self, image):
        """load the image and check it's size
        if the width is bigger than 500 -> then resize it to maximum width of 500 pixel
        if width is <= 500 -> return the same image"""
        image.load()

        self.width, self.height = image.size

        if self.width > 500:
            self.ratio = (self.width - 500) / 500
            self.width = 500
            self.height = self.height * self.ratio
            return image.resize(self.width, self.height)

        return image

    def make_meme(self, text, author, width=500) -> str:

        self.width = width

        """ add text to the image """
        im = ImageDraw.Draw(self.img)
        x = self.rand_x
        y = self.rand_y
        im.text((x, y), text, font=ImageFont.truetype('arial.ttf', 50),
                fill=(self.rand_val, self.rand_val, 255))

        im.text((x + 30, y + 50), author, font=ImageFont.truetype('arial.ttf', 50),
                fill=(255, 255, 255))
        img_name = datetime.today().strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'

        if not os.path.exists(self.path_of_saved_images):
            os.makedirs(self.path_of_saved_images)
        self.path_of_saved_images += img_name
        self.img.save(self.path_of_saved_images)

        return self.path_of_saved_images

    """ this property function is to choose a random x value for the text """
    @property
    def rand_x(self):
        return random.randint(0, self.width/2)

    """ random y value """
    @property
    def rand_y(self):
        return random.randint(0, self.height/2)

    @property
    def rand_val(self):
        return random.randint(0, 255)
