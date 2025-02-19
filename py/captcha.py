import requests
import base64
import pytesseract
from PIL import Image
import cv2
import time
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
s = requests.Session()
r = s.get("http://challenge01.root-me.org/programmation/ch8/index.php")
req = r.text
my_list = req.split('"')
src = my_list[1]
my_url_enc = src.split(',')[1]
my_url_enc_bytes = bytes(my_url_enc, 'utf-8')
with open("captcha.png", "wb") as fh:
    fh.write(base64.decodebytes(my_url_enc_bytes))

def solve_captcha(image_path):
    captcha_image = Image.open(image_path)
    captcha_text = pytesseract.image_to_string(captcha_image)
    return captcha_text
captcha_solution = solve_captcha('captcha.png')
captcha_solution = ''.join([c for c in captcha_solution if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"])
print(captcha_solution)
rep = s.post("http://challenge01.root-me.org/programmation/ch8/index.php", data={'cametu': captcha_solution})
print(rep.text[:350])
