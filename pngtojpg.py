#Conversion from a png image to a jpg one.
#You need to install pillow by pip install pillow

from PIL import Image
im = Image.open("path\image.png")
im.mode
'P'
im = im.convert('RGB')
im.mode
'RGB'
im.save('converted.jpg', quality=95)
