import cv2 
img = cv2.imread('D:\\AI\\17.2 - Computer Vision\\Data\\img0.jpg',0)
print('\t\tThe Image 1 Is When Using Grayscale :\n',img)
print('***'*30) 
img1 = cv2.imread('D:\\AI\\17.2 - Computer Vision\\Data\\img0.jpg',1)
print('\t\tThe Image 1 Is When Using Color(RGB) :\n',img1)
#Show Image 
#Display Img1 
cv2.imshow('Fisrt Image ',img)
k = cv2.waitKey(0)
if k == 27 : cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Image_01.jpg',img)
    cv2.destroyAllWindows()
#--------------------------------------------------------------------------------------------
import cv2 
img = cv2.imread('D:\\AI\\17.2 - Computer Vision\\Data\\img0.jpg',0)
print('\t\tThe Image 1 Is When Using Grayscale :\n',img)
print('***'*30) 
img1 = cv2.imread('D:\\AI\\17.2 - Computer Vision\\Data\\img0.jpg',1)
#print('\t\tThe Image 1 Is When Using Color(RGB) :\n',img1)
#Show Image 
#Display Img1 
# When You Nedd close image after limited duration using --> cv2.waitkey(5000)
# 5000 --> Is Meaning 5 Seconds
# And you must to put --> cv2.destroryAllWindows()
cv2.imshow('Fisrt Image ',img1)
k = cv2.waitKey(5000)
cv2.destroyAllWindows()
if k == 27 : cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Image_01.jpg',img1)
    cv2.destroyAllWindows()
