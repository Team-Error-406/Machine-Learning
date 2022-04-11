import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:\\Users\\Amresh Ranjan\\Desktop\\WEB DEVLOPS\\Image to Text Project\\tesseract.exe"

img_1 = cv2.imread("account_no.jpg")
word_1 = pytesseract.image_to_string(img_1)

img_2 = cv2.imread("cheque_no.jpg")
word_2 = pytesseract.image_to_string(img_2)

img_3 = cv2.imread("date.jpg")
word_3 = pytesseract.image_to_string(img_3)

img_4 = cv2.imread("pay.jpg")
word_4 = pytesseract.image_to_string(img_4)

img_5 = cv2.imread("rupee_in_digit.jpg")
word_5 = pytesseract.image_to_string(img_5)

img_6 = cv2.imread("ruppes_in_word.jpg")
word_6 = pytesseract.image_to_string(img_6)

# to save this model in o/p.

l1 = {'Account Number ' : word_1, 'Cheque Number ' : word_2, 'Date ' : word_3, 
		'Payer ' : word_4, 'Ruppes in Digits ' : word_5, 'Ruppes in Word ' : word_6}
with open("data.txt", 'w') as f: 
    for key, value in l1.items(): 
        f.write('%s:%s\n' % (key, value))

