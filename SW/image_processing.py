# External module imports
import cv2
import imutils
import pytesseract
import numpy as np
from time import sleep

# Internal functions
def get_grayscale(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
	return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #return cv2.adaptiveThreshold(image, 100, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 16)

def opening(image):
	kernel = np.ones((5, 5), np.uint8)
	return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def filter_plate(text):
    k = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -—";
    getVals = list(filter(lambda x:x in k, text))
    result = "".join(getVals)
    
    return result

# Definition of the function
def process_image():
	image = cv2.imread('tablica.jpg')
	image = imutils.resize(image, width=600 )
	#image = get_grayscale(image)
	#image = thresholding(image)
	#image = opening(image)
	
#	cv2.imshow("1. original image", image)
#	cv2.imwrite("1_original_image.png", image)
#	cv2.waitKey(0)
	
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#	cv2.imshow("2. greyed image", gray_image)
#	cv2.imwrite("2_greyed_image.png", gray_image)
#	cv2.waitKey(0)

	gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
#	cv2.imshow("3. smoothened image", gray_image)
#	cv2.imwrite("3_smoothened_image.png", gray_image)
#	cv2.waitKey(0)

	edged = cv2.Canny(gray_image, 30, 200)
#	cv2.imshow("4. edged image", edged)
#	cv2.imwrite("4_edged_image.png", edged)
#	cv2.waitKey(0)

	cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	image1=image.copy()
	cv2.drawContours(image1,cnts,-1,(0,255,0),3)
#	cv2.imshow("5. contours",image1)
#	cv2.imwrite("5_contours.png",image1)
#	cv2.waitKey(0)

	cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
	screenCnt = None
	image2 = image.copy()
	cv2.drawContours(image2,cnts,-1,(0,255,0),3)
#	cv2.imshow("6. Top 30 contours",image2)
#	cv2.imwrite("6_Top_30_contours.png",image2)
#	cv2.waitKey(0)

	i=7
	for c in cnts:
        	perimeter = cv2.arcLength(c, True)
        	approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        	if len(approx) == 4:
                	screenCnt = approx

        	x, y, w, h = cv2.boundingRect(c)
        	new_img = image[y:y + h, x:x + w]
        	cv2.imwrite('./' + str(i) + '.png', new_img)
        	i += 1
        	break

	Cropped_loc = cv2.imread('7.png')
	Cropped_loc = cv2.resize(Cropped_loc, (0, 0), fx=3, fy=3)
#	cv2.imshow("7. cropped", Cropped_loc)
#	cv2.imwrite("7_cropped.png", Cropped_loc)
#	cv2.waitKey(0)
	
	gray = get_grayscale(Cropped_loc)
#	cv2.imshow("8. grayed image", gray)
#	cv2.imwrite("8_grayed_image.png", gray)
#	cv2.waitKey(0)
	
	thresh = thresholding(gray)
#	cv2.imshow("9. thresholding image", thresh)
#	cv2.imwrite("9_thresholding_image.png", thresh)
#	cv2.waitKey(0)
	
	thresh = opening(thresh)
#	cv2.imshow("10. opened image", thresh)
#	cv2.imwrite("10_opened_image.png", thresh)
#	cv2.waitKey(0)
	
	thresh = cv2.GaussianBlur(thresh, (11, 11), 0)
#	cv2.imshow("11. gaussian image", thresh)
#	cv2.imwrite("11_gaussian_image.png", thresh)
#	cv2.waitKey(0)
	
	thresh = cv2.medianBlur(thresh, 9)
#	cv2.imshow("12. ready image", thresh)
#	cv2.imwrite("12_ready_image.png", thresh)
#	cv2.waitKey(0)
	
	config = r"--psm 10"# --oem 3"
	plate = pytesseract.image_to_string(thresh, config = config)
	
	plate = filter_plate(plate)
	
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()

	return plate
