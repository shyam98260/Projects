from random import randint
from captcha.image import ImageCaptcha
from PIL import Image


def generate_captcha():
    image = ImageCaptcha()
    a = str(
        str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(
            randint(0, 9)))
    image.write(a, 'shyam.png')

    img = Image.open('shyam.png')
    new_width = 190
    new_height = 40

    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save('shyam.png')
    return a
