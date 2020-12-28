from datetime import datetime
from io import BytesIO
from PIL import Image 
import base64

def b64_img(file):
    starter = file.find(',')
    image_data = file[starter+1:]
    image_data = bytes(image_data, encoding="ascii")
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    name = 'static/' + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + '.png'
    im.save(name)
    return name