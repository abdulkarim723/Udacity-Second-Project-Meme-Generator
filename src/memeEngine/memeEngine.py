from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random


class memeEngine:
    def __init__(self, path_to_image, text):
        self.width = 0
        self.height = 0
        self.ratio = 1.0
        """ load the image """
        img = Image.open(path_to_image)
        img.load()

        self.width, self.height = img.size

        if self.width > 500:
            self.ratio = (self.width - 500)/500
            self.width = 500
            self.height = self.height * self.ratio
            img = img.resize(self.width, self.height)

        im = ImageDraw.Draw(img)
        im.text((self.rand_x, self.rand_y), text, font=ImageFont.truetype('arial.ttf', 50),
                fill=(self.rand_val, self.rand_val, self.rand_val))

        img.show()

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
