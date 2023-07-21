import mediapipe
import cv2
from protobuf_to_dict import protobuf_to_dict

    
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:

    while True:
        ret, frame = cap.read()
        #frame = cv2.imread('C:/Users/saikk/Pictures/Camera Roll/Laptop camera image.jpg', 0)
        frame1 = cv2.resize(frame, (640, 480))
        results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
        
        if results.multi_hand_landmarks != None:
           for handLandmarks in results.multi_hand_landmarks:
               drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
               
           for landmark in results.multi_hand_landmarks:
                c = 0
                sum_x = 0
                sum_y = 0
                for i in landmark.landmark:
                    sum_x+=i.x
                    sum_y+=i.y
                    c+=1
                avg_x = sum_x/c
                avg_y = sum_y/c
                print(c)
                if(avg_x<avg_y and avg_x+avg_y<1.2):
                    print('MOVE RIGHT')
                elif(avg_x<avg_y and avg_x+avg_y>1.2):
                    print('MOVE DOWN')
                elif(avg_x>avg_y and avg_x+avg_y<1.2):
                    print('MOVE UP')
                elif(avg_x>avg_y and avg_x+avg_y>1.2):
                    print('MOVE LEFT')
    
        cv2.imshow("Frame", frame1);
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("q"):
           break
cv2.destroyAllWindows()
