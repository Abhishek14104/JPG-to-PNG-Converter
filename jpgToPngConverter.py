import sys
import os
from PIL import Image, ImageFilter
imageFolder = sys.argv[1]
outputFolder = sys.argv[2]

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

for filename in os.listdir(imageFolder):
    img = Image.open(f'{imageFolder}{filename}')
    splitName = os.path.splitext(filename)[0]
    imgSave = img.save(f'{outputFolder}{splitName}.png', 'png')
    print('All Done!')
    
# Run this code by using 
# python .\jpgToPngConverter.py pokedex\ new\
# this in the command line