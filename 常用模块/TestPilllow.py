from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def fultertest():
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open('常用模块/test.jpg')
    # 应用模糊滤镜:
    im2 = im.filter(ImageFilter.GaussianBlur)
    im2.save('常用模块/blur2.jpg', 'jpeg')
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def vercodetest():
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('BOD_BLAI.TTF', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.EMBOSS)
    image.save('常用模块/code.jpg', 'jpeg')
if __name__ == '__main__':
    vercodetest()