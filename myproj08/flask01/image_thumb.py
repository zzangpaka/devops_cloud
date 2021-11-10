# pip install pillow

from PIL import Image


im = Image.open("static/alpaca.jpg")
im.thumbnail((800, 600))
im.save("static/alpaca.jpg")
