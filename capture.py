import cv2

def capture(name, threshold):
    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
    
    #https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    cap = cv2.VideoCapture(0)
    
    i=0
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
        #for (x,y,w,h) in faces:
        #    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #    roi_gray = gray[y:y+h, x:x+w]
        #    roi_color = img[y:y+h, x:x+w]
            
        eyes = eye_cascade.detectMultiScale(gray, 1.1, 10, 0, (200, 150))
        
        ex = 0; ey = 0; ew = 0; eh = 0;
        if len(eyes) > 0:
            ex,ey,ew,eh = eyes[0];
            
            image = cv2.cvtColor(img[ey:ey+eh, ex:ex+ew], cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(image, cv2.CV_64F).var()
            if fm < threshold :
                cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            else:
                cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
                cv2.imwrite('{}/{}_{}.png'.format(name, i, fm), img[ey:ey+eh, ex:ex+ew])
                i += 1
    
        cv2.imshow('Camera',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()