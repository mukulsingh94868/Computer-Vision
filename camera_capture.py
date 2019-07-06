import cv2

cap=cv2.VideoCapture(0)
print(cap.isOpened())

while cap.isOpened():
    status,frame=cap.read()
    # convert coler into gray scale
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    print(frame.shape)

    # now we can draw all those patterns
    # line
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
    # rectangle
    cv2.rectangle(frame,(50,50),(250,300),(0,0,255),2)
    # circle
    cv2.circle(frame,(200,300),200,(13,44,123),2)
    # text
    font = cv2.FONT_HERSHEY_SIMPLEX # this fount type
    cv2.putText(frame,'dipesh',(10,50), font, 2,(0,2,55),2,cv2.LINE_AA)
    cv2.imshow('live',frame-60)
    #cv2.imshow('live1',frame)
    #cv2.imshow('live2',frame)
    #cv2.imshow('live3',frame)
    #cv2.imshow('live4',grayimg)
    if cv2.waitKey(10) & 0xff == ord('q') : # q se window bande ho jae gi
        break

# distroy ker ne ke liye
cv2.destroyAllWindows()

cap.release()
