import src.core.io as io
from PIL import Image


obj = io.load_image("../../tests/1/field/0.tif")
array = io.get_image_vector(obj)
arraytest = list()
for row in array:
    new_row = list()
    for val in row:
        if val > 100:
            new_row.append(255)
        else:
            new_row.append(0)
    arraytest.append(new_row)

io.show_image(Image.fromarray(io.get_image_vector(arraytest)))