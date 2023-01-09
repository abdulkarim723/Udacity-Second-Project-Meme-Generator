from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random


class MemeEngine:
    def __init__(self, image_path):
        self.img = None
        self.width = 0
        self.height = 0
        self.ratio = 1.0
        self.width = 500
        self.height = 500
        self.path_of_saved_images = image_path
        self.path_of_saved_image = None

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

    def make_meme(self, path, text, author, width=500) -> str:

        self.path_of_saved_image = self.path_of_saved_images + path.split('/')[-1]
        self.width = width

        """ load the image """
        self.img = Image.open(path)

        """ setup the image size """
        self.img = self.setup_image_size(self.img)

        """ add text to the image """
        im = ImageDraw.Draw(self.img)
        x = self.rand_x
        y = self.rand_y
        im.text((x, y), text, font=ImageFont.truetype('arial.ttf', 50),
                fill=(self.rand_val, self.rand_val, 255))

        im.text((x + 30, y + 50), author, font=ImageFont.truetype('arial.ttf', 50),
                fill=(255, 255, 255))

        self.img.save(self.path_of_saved_image)

        return self.path_of_saved_image

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

"""
if __name__ == '__main__':
    meme = MemeEngine('./files')
    meme.make_meme('../_data/photos/dog/xander_1.jpg', "hello world", "author")
"""