import cv2
import pytesseract
import re
import numpy as np
#plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
plate_cascade = cv2.CascadeClassifier('/Users/yojhu/Desktop/train_plates/output/cascade.xml')

#img = cv2.imread('car_example1.jpg')
#img = cv2.imread('car_example2.jpg')
#img = cv2.imread('car_example3.jpg')
img=cv2.imread('car_example4.jpg')
#img=cv2.imread('not_car.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plates = plate_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6,minSize=(20, 20))
#print(plates)
count=0
if len(plates) == 0:
    print("未偵測到車牌")
    count=count+1
else:
    for (x, y, w, h) in plates:
        plate_roi = gray[y-4:y+h+4,x-6:x+w+6]
        plate_roi = cv2.bilateralFilter(plate_roi, 11, 17, 17)
        plate_roi = cv2.GaussianBlur(plate_roi, (3, 3), 0)
        ret, plate_roi = cv2.threshold(plate_roi, 127, 255, cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(plate_roi, config='--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        text = text.replace(" ", "")
        #print(text)
        #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = re.sub(r'[^A-Z0-9]', '', text.upper())
        match = re.search(r'[A-Z0-9]{5,9}', text)
        if match:
            count=count+1 
            cv2.rectangle(img, (x-6,y-4), (x+w+6,y+h+4), (0, 255, 0), 2)
            print(f"偵測到車牌文字: {text}")
        
if(count==0):
    print("未偵測出車牌")
cv2.imshow('車牌位置', img)
cv2.waitKey(0)
cv2.destroyAllWindows()