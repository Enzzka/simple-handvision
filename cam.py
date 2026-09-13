import cv2
from cvzone.HandTrackingModule import HandDetector

current_mode = 0
total_modes = 6
pinky_touching = False

cam = cv2.VideoCapture(0)

detector = HandDetector(maxHands=2, detectionCon=0.4)

while True:

    success, frame = cam.read()

    if not success:
        continue

    hands, frame = detector.findHands(frame)

    
    if hands:
        
        # Hands
        my_hand1 = hands[0]
        lmlist1 = my_hand1["lmList"]
 
        thumb_tip1 = lmlist1[4]
        index_tip1 = lmlist1[8]
        pinky_tip1 = lmlist1[20]

        distance, _, frame = detector.findDistance(thumb_tip1[:2], pinky_tip1[:2], frame)

        thumb1_x, thumb1_y = thumb_tip1[0], thumb_tip1[1]
        index1_x, index1_y = index_tip1[0], index_tip1[1]

        if len(hands) == 2:
            my_hand2 = hands[1]
            lmlist2 = my_hand2["lmList"]

            thumb_tip2 = lmlist2[4]
            index_tip2 = lmlist2[8]

            thumb2_x, thumb2_y = thumb_tip2[0], thumb_tip2[1]
            index2_x, index2_y = index_tip2[0], index_tip2[1]

            if distance < 20:
                if not pinky_touching:
                    current_mode = (current_mode + 1) % total_modes
                pinky_touching = True
            else:
                pinky_touching = False

                if current_mode == 1:
                    cv2.line(frame, (index1_x, index1_y), (index2_x, index2_y), (255, 255, 255), 2)
                    cv2.line(frame, (thumb1_x, thumb1_y), (thumb2_x, thumb2_y), (255, 255, 255), 2)
                    cv2.line(frame, (index1_x, index1_y), (thumb1_x, thumb1_y), (255, 255, 255), 2)
                    cv2.line(frame, (index2_x, index2_y), (thumb2_x, thumb2_y), (255, 255, 255), 2)

                elif current_mode == 2:
                    
                    cv2.rectangle(frame, (index1_x, index1_y), (index2_x, index2_y), (255, 255, 255), 2)
                
                elif current_mode == 3:

                    cv2.arrowedLine(frame, (index1_x, index1_y), (index2_x, index2_y), (255, 255, 255), 3)
                
                elif current_mode == 4:

                    cv2.arrowedLine(frame, (index2_x, index2_y), (index1_x, index1_y), (255, 255, 255), 3)
                
                elif current_mode == 5:
                    cv2.drawMarker(frame, (index1_x, index1_y), (255, 255, 255), cv2.MARKER_CROSS, markerSize=30, thickness=2)
                    cv2.drawMarker(frame, (index2_x, index2_y), (255, 255, 255), cv2.MARKER_CROSS, markerSize=30, thickness=2)


    frame = cv2.flip(frame, 1)

    cv2.putText(frame, f"MODE: {current_mode}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)


            # box_pixel = frame[index1_y : index2_y, index1_x, index2_x]
            # lab_box = cv2.cvtColor(box_pixels, cv2.COLOR_BGR2LAB)


    cv2.imshow("Cam:", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cam.release()
cv2.destroyAllWindows()