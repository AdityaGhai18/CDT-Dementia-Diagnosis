##combined script using functions
#getting libs
import os 
import numpy as np
import cv2

directory = r'/Users/adityaghai/Desktop/10 photo test'
os.chdir(directory)
file_name = '10004334.tif'

#image needs to be brought in as file_name

def part1():
    img1 = cv2.imread(file_name)
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    thresh_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    # Blur the image
    blur = cv2.GaussianBlur(thresh_inv,(1,1),0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    # find contours
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    mask = np.ones(img1.shape[:2], dtype="uint8") * 255
    for c in contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        if w*h>1000:
            cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 0, 255), -1)
    step1 = cv2.bitwise_and(img1, img1, mask=cv2.bitwise_not(mask))
    part1resultpath = r'/Users/adityaghai/Desktop/image processing clock/Processing Files/Part1_result'
    os.chdir(part1resultpath)
    cv2.imwrite(file_name, step1)

def part2():
    file_name2 = r'/Users/adityaghai/Desktop/image processing clock/Processing Files/Part1_result/' + file_name
    print(file_name2)
    img2 =  cv2.imread(file_name2)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #Separate the background from the foreground
    bit = cv2.bitwise_not(gray2)
    #Apply adaptive mean thresholding
    amtImage = cv2.adaptiveThreshold(bit, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 15)
    #Apply erosion to fill the gaps
    kernel = np.ones((15,15),np.uint8)
    erosion = cv2.erode(amtImage,kernel,iterations = 2)
    #Take the height and width of the image
    (height, width) = img2.shape[0:2]
    #Ignore the limits/extremities of the document (sometimes are black, so they distract the algorithm)
    image = erosion[50:height - 50, 50: width - 50]
    (nheight, nwidth) = image.shape[0:2]
    #Create a list to save the indexes of lines containing more than 20% of black.
    index = []
    for x in range (0, nheight):
        line = []
            
        for y in range(0, nwidth):
            line2 = []
            if (image[x, y] < 150):
                line.append(image[x, y])
        if (len(line) / nwidth > 0.2):    
            index.append(x)
    #Create a list to save the indexes of columns containing more than 15% of black.
    index2 = []
    for a in range(0, nwidth):
        line2 = []
        for b in range(0, nheight):
            if image[b, a] < 150:
                line2.append(image[b, a])
        if (len(line2) / nheight > 0.15):
            index2.append(a)
   
    #Crop the original image according to the max and min of black lines and columns.
    step2 = img2[min(index):max(index) + min(250, (height - max(index))* 10 // 11) , max(0, min(index2)): max(index2) + min(250, (width - max(index2)) * 10 // 11)]
    #########
    #Save the image
    part2resultpath = r'/Users/adityaghai/Desktop/image processing clock/Processing Files/Part2_result'
    os.chdir(part2resultpath)
    cv2.imwrite(file_name, step2)

def part3():
    file_name3 = r'/Users/adityaghai/Desktop/image processing clock/Processing Files/Part2_result/' + file_name
    src = cv2.imread(file_name3, 1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    step3 = cv2.merge(rgba,4)
    part3resultpath = r'/Users/adityaghai/Desktop/image processing clock/Processing Files/Part3_result'
    os.chdir(part3resultpath)
    cv2.imwrite(file_name, step3)
    


#getting filenames for first batch might need to be after all the functions, we'll see
part1()
part2()
part3()


