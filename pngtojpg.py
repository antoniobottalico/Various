#COnversion from a png image to a jpg one.

from PIL import Image
im = Image.open("path\image.png")
im.mode
'P'
im = im.convert('RGB')
im.mode
'RGB'
im.save('converted.jpg', quality=95)
