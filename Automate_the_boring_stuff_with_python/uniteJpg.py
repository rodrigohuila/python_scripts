#! /usr/bin/python3


import os
import img2pdf

# convert all files ending in .jpg inside a directory
dirname = "/home/rodrigo/Downloads/Test"
os.chdir(dirname)
with open("name.pdf", "wb") as f:
    imgs = []
    for fname in os.listdir(dirname):
        if not fname.endswith(".jpg"):
            continue
        path = os.path.join(dirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)
    f.write(img2pdf.convert(imgs))
