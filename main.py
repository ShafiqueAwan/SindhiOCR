import cv2
import argparse
import pytesseract

from PIL import Image
from time import time

# add argument parser for images
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', help='path to .jpg file')
args = vars(ap.parse_args())

#start timer
start_time = time()
print ('Start OCR Scanning')

# read image from arguments
image = cv2.imread(args['image'])

# process image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold, image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

# extract text from image
image = Image.fromarray(image)
text = pytesseract.image_to_string(image, lang='ara')

# write text to file
with open("Output.TXT", "w") as file:
    file.write(text)

#end timer
end_time = time() - start_time
print ('Scanning ended in {} seconds'.format(round(end_time, 2)))


