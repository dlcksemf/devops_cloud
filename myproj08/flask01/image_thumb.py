from PIL import Image

im = Image.open("static/christmas.jpg")
im.thumbnail((800, 600))
im.save("static/christmas.jpg")
