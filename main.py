from ultralytics import YOLO
import cv2
import math
import serial
import time
cap=cv2.VideoCapture(0)



frame_width=int(cap.get(3))
frame_height = int(cap.get(4))

out=cv2.VideoWriter('resultados_prueba/v1/output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

model=YOLO("../modelos/bestV19.pt")
classNames = ["1PHelmet","1PNoHelmet","1PNoHelmet1PHelmet","2PHelmet","2PNoHelmet","3P","plate"]
classIle= ["1PNoHelmet","1PNoHelmet1PHelmet","3P"]



ser = serial.Serial("COM6",9600)

while True:
    success, img = cap.read()

    results=model(img,stream=True)

    detections = False
    for r in results:
        boxes=r.boxes
        for box in boxes:
            detections = True
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
            print(x1,y1,x2,y2)
            conf=math.ceil((box.conf[0]*100))/100
            if(conf > 0.65):
                cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,255),3)
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1,y1), c2, [255,0,255], -1, cv2.LINE_AA) 
                cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)
                if class_name in classIle:
                    ser.write(b'1')

                else:
                    ser.write(b'2')
                if not detections:
                    ser.write(b'2')
                    

    out.write(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord('1'):
        break
out.release()
