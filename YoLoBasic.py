from ultralytics import YOLO
import cv2 as cv
import cvzone as cz
import math

# cap = cv.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
cap = cv.VideoCapture("video/Example1.mp4")
model = YOLO("YoLo_Weight/yolov8n.pt")
className = ["person",'bicycle','car','motorbike','aeroplane','bus','train','truck','boat','traffic light','fire hydrant','stop sign','parking meter','bench','bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe','backpack','umbrella','handbag','tie','suitcase','frisbee','skis','snowboard','sports ball','kite','baseball bat','baseball glove','skateboard','surfboard','tennis racket','bottle','wine glass','cup','fork','knife','spoon','bowl','banana','apple','sandwich','orange','broccoli','carrot','hot dog','pizza','donut','cake','chair','sofa','pottedplant','bed','diningtable','toilet','tvmonitor','laptop','mouse','remote','keyboard','cell phone','microwave','oven','toaster','sink','refrigerator','book','clock','vase','scissors','teddy bear','hair drier','toothbrush']

while True:
    success, img = cap.read()
    result = model (img,stream=True)
    for r in result:
        boxes = r.boxes
        for box in boxes:
            #Bouding
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            # cv.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)  
            w,h = x2-x1,y2-y1
            cz.cornerRect(img,(x1,y1,w,h))
            conf = math.ceil((box.conf[0])*100)/100
            
            #class
            cls = int(box.cls[0])
            
            cz.putTextRect(img,f'{className[cls]} {conf}',(max(0,x1),max(35,y1)),scale=1, thickness=1)
    cv.imshow("Image",img)
    cv.waitKey(1)
