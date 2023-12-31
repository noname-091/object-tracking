import cv2

cap = cv2.VideoCapture(0)

# new_width = 720
# new_height = 720

tracker = cv2.legacy.TrackerMedianFlow.create()

success, img = cap.read()
# img2 = cv2.resize(img, (new_width, new_height))
bbox = cv2.selectROI('tracking', img, False)
tracker.init(img, bbox)

def drawBox(img, bbox):
    x,y,h,w = int(bbox[0]),int (bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x,y),((x+h), (y+w)),(255,0,255),3,1)


while True:

    timer = cv2.getTickCount()
    success, img = cap.read()
    # img = cv2.resize(img, (new_width, new_height))


    success, bbox = tracker.update(img)
    # print(bbox)
    if success:
        drawBox(img, bbox)
        
    else: 
        cv2.putText(img, "Lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, str(int(fps)), (75, 50), cv2.FONT_ITALIC, 0.7, (0, 0, 255), 2)
    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
