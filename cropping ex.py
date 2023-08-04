from PIL import image

image = "monster"

img = image.open(image)

box = (250, 250, 750, 750)

img2 = img.crop(box)

img2.save('myimage_cropped')

img.show()
