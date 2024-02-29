import os
from PIL import Image


def unpremultiply(image_path):
    img = Image.open(image_path)
    img_data = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b, a = img_data[x, y]

            if a != 0:
                r = int((255 * r) / a)
                g = int((255 * g) / a)
                b = int((255 * b) / a)

            img_data[x, y] = (r, g, b, a)

    img.save(f"{os.path.splitext(image_path)[0]}_unpremultiplied.png")


def premultiply(image_path):
    img = Image.open(image_path)
    img_data = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b, a = img_data[x, y]

            r = int((r * a) / 255)
            g = int((g * a) / 255)
            b = int((b * a) / 255)

            img_data[x, y] = (r, g, b, a)

    img.save(f"{os.path.splitext(image_path)[0]}_premultiplied.png")