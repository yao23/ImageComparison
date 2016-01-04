import os,sys
from PIL import Image
jpgfile = Image.open("./baybridge.jpg")

print jpgfile.bits, jpgfile.size, jpgfile.format

# print "Hello World"
