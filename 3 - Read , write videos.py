import cv2 
capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('Movie.avi',fourcc,20.0 , (640,480))
print(capture.isOpened())
while(capture.isOpened()):
    ret , frame = capture.read()
    if ret == True:
        print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        output.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xff==ord('q'): break 
    else : break 
capture.release()
output.release()
cv2.destroyAllWindows()