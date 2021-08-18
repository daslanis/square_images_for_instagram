import PIL
from PIL import Image

def make_images_square(path):
    test = PIL.Image.open(path)

    eikona = PIL.Image.open(path)
    width , height = eikona.size

    if(width != height):
        if(width < height):
            new_size = height
            nea_eikona = PIL.Image.new("RGBA", (new_size, new_size), (255, 255, 255, 255))
            nea_eikona.paste(test, (int((new_size/2) - (width/2)), 0))
        else:
            new_size = width
            nea_eikona = PIL.Image.new("RGBA", (new_size, new_size), (255, 255, 255, 255))
            nea_eikona.paste(test, (0, int((new_size/2) - (height/2))))

    nea_eikona.save("new_" + str(path))

    eikona.close()
    nea_eikona.close()

make_image_square("image.png")
