from random import choice

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import cv2
import pytesseract



def text_recognition(message: types.Message, state: FSMContext) -> None:
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    c = 0; 
    for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    cv2.imwrite("crop"+str(c)+".jpeg",cropped) 
    c+=1
    cv2.imwrite('rectanglebox.jpg',rect)

    image = cv2.imread("test.png")

    enhancer1 = ImageEnhance.Sharpness(image)
    factor1 = 0.01
    im_s_1 = enhancer1.enhance(factor1)
    
    balance = pytesseract.image_to_string(cropped, config='outputbase digits')

    file.write(text) 
    file.write("\n")

    file.close 
    await message.answer(text)






