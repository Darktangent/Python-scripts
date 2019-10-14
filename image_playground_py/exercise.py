from PIL import Image, ImageFilter
import sys
import os
# img = Image.open('./pokedex/')

folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)
for filename in os.listdir(folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f"{folder}{filename}")
    img.save(f"{new_folder}/{clean_name}.png", "png")
    print("all done")
