#HSV-hue saturation value
#rgb - its intensity
#hue= basepigment ranges 0-360 base of the cone
# saturation - amount of hue or color fron centre to outer later0-100%
#  value - brightness of the color
import cv2
import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture(0);

cv2.namedWindow("tracking")
cv2.createTrackbar("LH","tracking",0,255,nothing)
cv2.createTrackbar("Ls","tracking",0,255,nothing)
cv2.createTrackbar("Lv","tracking",0,255,nothing)
cv2.createTrackbar("UH","tracking",0,255,nothing)
cv2.createTrackbar("Us","tracking",255,255,nothing)
cv2.createTrackbar("UV","tracking",255,255,nothing)

while True:
    frame = cv2.imread("smarties.jpeg")
    #_,frame = cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("LH","tracking")
    l_s=cv2.getTrackbarPos("Ls","tracking")
    L_V = cv2.getTrackbarPos("Lv", "tracking")

    U_h = cv2.getTrackbarPos("UH", "tracking")
    u_s=cv2.getTrackbarPos("Us","tracking")
    U_v = cv2.getTrackbarPos("UV", "tracking")

    l_b=np.array([l_h,l_s,L_V])
    u_b=np.array((U_h,u_s,U_v))
    mask= cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("rest",res)
    #cv2.imshow("hsv",hsv)
    key = cv2.waitKey(1)
    if key ==27:
        break
cap.release()
cv2.destroyAllWindows()