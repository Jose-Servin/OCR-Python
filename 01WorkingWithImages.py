""" Module providing a sandbox env for OCR Introduction. """
from PIL import Image
import cv2

IM_PATH = "./data/page_01.jpg"
IM_TEMP = "./temp/"

with Image.open(IM_PATH) as im:
    im.show()
