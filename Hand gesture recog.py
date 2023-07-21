import cv2
from collections import Counter
from module import findnameoflandmark,findpostion,speak
import math

cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]

while True:
         ret, frame = cap.read() 
         frame1 = cv2.resize(frame, (640, 480))
        
         a=findpostion(frame1)
         b=findnameoflandmark(frame1)
         #print(b)
    
         
         if len(b and a)!=0:
            finger=[]
            fingers_up = []
            if a[2][1:] < a[4][1:]: 
               finger.append(1)
               fingers_up.append(b[4])
               #print (b[4])
              
            else:
               finger.append(0)   
            
            fingers=[] 
            
            for id in range(0,4):
                if a[tip[id]][2:] < a[tip[id]-2][2:]:
                   #print(b[tipname[id]])
                   fingers_up.append(b[tipname[id]])
    
                   fingers.append(1)
        
                else:
                   fingers.append(0)
            if(len(fingers_up) == 0):
                print("STOP")
            elif(len(fingers_up) == 1):
                if('THUMB TIP' in fingers_up):
                    print("MOVE UP")
            elif(len(fingers_up) == 2):
                if(all(i in fingers_up for i in ['THUMB TIP','INDEX FINGER TIP'])):
                    print("MOVE LEFT")
                elif(all(i in fingers_up for i in ['THUMB TIP','PINKY TIP'])):
                    print("MOVE RIGHT")
            elif(len(fingers_up) == 3):
                if(all(i in fingers_up for i in ['MIDDLE FINGER TIP','RING FINGER TIP','PINKY TIP'])):
                    print("MOVE DOWN")
         x=fingers + finger
         c=Counter(x)
         up=c[1]
         down=c[0]
    #     print('This many fingers are up - ', up)
    #     print('This many fingers are down - ', down)
         
         
         cv2.imshow("Frame", frame1);
         key = cv2.waitKey(1) & 0xFF
         
         
         if key == ord("q"):
            speak("you have"+str(up)+"fingers up  and"+str(down)+"fingers down") 
         
         if key == ord("s"):
           break
cv2.destroyAllWindows()