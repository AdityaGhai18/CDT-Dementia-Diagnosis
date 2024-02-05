import cv2
import os
file_name = "/Users/adityaghai/Desktop/savedImage.jpg"

src = cv2.imread(file_name, 0)
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(src)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)

directory = r'/Users/adityaghai/Desktop'
os.chdir(directory)
cv2.imwrite("backgroundremoved.png", dst)