#-*- coding:utf8 -*-
from PIL import Image
import hashlib
import time


# read image file
im = Image.open("captcha.gif")
im.convert("P")

# change colour to black(1) & white(256)
im2 = Image.new("P", im.size, 255)
for x in range(im.size[0]):
    for y in range(im.size[1]):
        pix = im.getpixel((x,y))
        if pix == 220 or pix == 227:
            im2.putpixel((x,y), 0)

im2.show()
print im2.histogram()

# find the letters
inletter = False
foundletter = False
start, end = 0, 0
letters = []

for x in range(im2.size[0]):
    for y in range(im2.size[1]):
        pix = im2.getpixel((x,y))
        if pix != 255:
            inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = x
    
    if foundletter == True and inletter == False:
        foundletter = False
        end = x
        letters.append((start, end))

    inletter = False

print letters


# cut the image into letters
count = 0

for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0], 0, letter[1], im2.size[1] ))
    m.update("{}{}".format(time.time(), count))
    im3.save("./{}.gif".format(m.hexdigest))
    count += 1













