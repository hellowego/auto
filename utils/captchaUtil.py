#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

class CaptchaUtil(object):
    """docstring for CaptchaUtil"""
    def __init__(self):
        super(CaptchaUtil, self).__init__()
        # self.arg = arg


    # 随机字母:
    def rndChar(self):
        return chr(random.randint(65, 90))

    # 随机颜色1:
    def rndColor(self):
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 随机颜色2:
    def rndColor2(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    def createCodeImage(self):

        # 240 x 60:
        width = 100
        height = 40
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 创建Font对象:
        font = ImageFont.truetype('Arial.ttf', 20)
        # 创建Draw对象:
        draw = ImageDraw.Draw(image)
        # 填充每个像素:
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=self.rndColor())
        # 输出文字:
        randstr = ""
        for t in range(4):
            randchar = self.rndChar()
            randstr = randstr + str(randchar)
            print randchar
            draw.text((25 * t + 5, 10), randchar, font=font, fill=self.rndColor2())
        print randstr
        # 模糊:
        # image = image.filter(ImageFilter.BLUR)
        # image.save('code.jpg', 'jpeg');
        return image,randstr



if __name__ == '__main__':
    img = CaptchaUtil()
    code_img= img.createCodeImage()
    code_img.save('xx.jpg','JPEG')



