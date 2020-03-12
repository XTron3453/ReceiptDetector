import cv2
import os
import pytesseract
from PIL import Image
import numpy as np
from itertools import chain
img = cv2.imread(r"Walmart Receipts\33612.png") #Replace with photo taken in the app
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)

items = text.split()
all_items = repr(text).split("\\n")
groceries = list()

target_track = False

identifier = 1 #Will replace with Machine Learning function

print(items)

if identifier == 0: 
	grocery_bool = False
	for item in items:
		if item.lower() == "grocery":
			grocery_bool = True
		if grocery_bool:
			if str.isdigit(item) and len(item) == 9:
				groceries.append(item) 
				
elif identifier == 1:
	for item in items:
		if str.isdigit(item) and len(item) == 12:
			groceries.append(item)


print(groceries)

