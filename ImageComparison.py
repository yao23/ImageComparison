import os,sys
from PIL import Image
jpgfile = Image.open("baybridge.jpg")

print jpgfile.bits, jpgfile.size, jpgfile.format

image = jpgfile
image = image.resize((8, 8), Image.ANTIALIAS)  # Reduce it's size.
image = image.convert("L")  # Convert it to grayscale.
pixels = list(image.getdata())
avg = sum(pixels) / len(pixels)
bits = "".join(map(lambda pixel: '1' if pixel > avg else '0', pixels))  # '00010100...'
hexadecimal = int(bits, 2).__format__('016x').upper()

print hexadecimal

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def getimagehash(image):
   image = image.resize((8, 8), Image.ANTIALIAS)  # Reduce it's size.
   image = image.convert("L")  # Convert it to grayscale.
   pixels = list(image.getdata())
   avg = sum(pixels) / len(pixels)
   bits = "".join(map(lambda pixel: '1' if pixel > avg else '0', pixels))  # '00010100...'
   hexadecimal = int(bits, 2).__format__('016x').upper()

   print hexadecimal

   hexdec = int(bits, 2)
   print hexdec
   return hexdec

image0 = Image.open("baybridge.jpg")
image1 = Image.open("baybridge1.jpg")
image2 = Image.open("baybridge2.jpg")
hex0 = getimagehash(image0)
hex1 = getimagehash(image1)
hex2 = getimagehash(image2)

print (hex0 - hex1)
print (hex0 - hex2)

# print "Hello World"
