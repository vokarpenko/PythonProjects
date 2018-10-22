def add_dataset():
    import cv2
    import os
    import trainer
    cam = cv2.VideoCapture(0)
    cam.set(3, 1280) # set video width
    cam.set(4, 720) # set video height
    face_detector = cv2.CascadeClassifier('face.xml')

    if os.listdir(path='dataset'):
        kolvo = 0
        f = open('names.txt', 'r')
        for line in f:
            kolvo += 1
        f.close()
        f = open('names.txt', 'a')
        f.write("%s\n" % input('\n Введите ваше имя: '))
        f.close()
        face_id = kolvo
    else:
        names= ['None']
        names.append(input('\n Введите ваше имя: '))
        face_id =1
        f = open('names.txt','w' )
        for item in names:
            f.write("%s\n" % item)
        f.close()
    print("\n Смотрите в камеру.")
    # Initialize individual sampling face count
    count = 0

    while(True):
        ret, img = cam.read()
        img = cv2.flip(img, 1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5, minSize=(100,100))

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            #cv2.imshow('image', img)
        cv2.imshow('video', img)
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 50 face sample and stop video
            trainer.create_yml()
            break

    # Do a bit of cleanup
    cam.release()
    cv2.destroyAllWindows()
    return