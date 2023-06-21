import cv2
print("Running")

#Storing harcascade path
harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) #width
cap.set(4, 480) #height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    # to load Cascade model
    plate_cascade = cv2.CascadeClassifier(harcascade)

    # Converting colour image to grayscale since opencv accepts ony grayscale img
    img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # to get plate coordinate
    plates = plate_cascade.detectMultiScale(img_grey, 1.1, 4) 
    # By default parameter are 1.1,4 coz they give better results

    for(x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            # creating detection boundary
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
            #   rectangle(img,(min_cordinates),(max_cordinates),(colorcode),thickness)
            #colorcode : R,G,B
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
             
             #to crop region of intrest(roi) Here:number plate
            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)
            # cv2.waitKey(0)
          
            # to show the img
    cv2.imshow("Result", img)
    # cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord('q'): #'letter to close cmaera window'
        break
 # to scan the cropped number plate
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results",img)
        cv2.waitKey(500)
        count += 1
        