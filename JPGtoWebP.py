from PIL import Image
import os

path = './images'
pathOut = './convertedImgs'


for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    img.convert('RGB')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{pathOut}/{clean_name}_converted.webp', format='webp')
    
    
    