# pip install rembg
# pip install -U Pillow

from rembg import remove
from PIL import Image

input = Image.open('C:\\project_images\\images_americancasual\\americancasual_img\\1-11.jpg') # load image
output = remove(input) # remove background
output.save('1-11bg.PNG') # save image