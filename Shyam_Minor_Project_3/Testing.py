from random import randint
from captcha.image import ImageCaptcha
image = ImageCaptcha()
a = str(str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9)))
image.write(a,'shyam.png')