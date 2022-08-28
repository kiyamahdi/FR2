from DataBase import DB
from RIG import GUI
import cv2
import face_recognition
import numpy as np
import os
import mediapipe as mp

Hand = mp.solutions.hands.Hands(max_num_hands=1)
file = os.getcwd()

def file_name_pictures():
    try:
        os.mkdir('img')
    except FileExistsError:
        pass
    path = 'img'
    images = []
    classname = []
    myList = os.listdir(path)
    #print(myList)
    for climg in myList:
        img = cv2.imread(f'{path}/{climg}')
        images.append(img)
        classname.append(os.path.splitext(climg)[0])
        #print(classname)
    return images, classname

def findEncodings():
    images, _ = file_name_pictures()
    encodlist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encod = face_recognition.face_encodings(img)[0]
        encodlist.append(encod)
    return encodlist

def creat_id():
    _, classname = file_name_pictures()
    if classname == []:
        classname.append(0)
    name = classname[-1]
    name = int(name)
    name = name + 1
    return name

def find_hand(frameRGB, w, h):
    out = []
    for id, lm in enumerate(frameRGB.landmark):
        if id in [8]:
            out.append((int(lm.x * w), int(lm.y * h)))
    return out

def show1():
    f = 0
    num = 60
    while True:
        img = cv2.imread(f"{file}//f.jpg")
        cv2.line(img, (60, 500), (700, 500), (255, 0, 0), 80)
        cv2.putText(img, "Hello", (250, 90), cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 102, 255), 2)
        cv2.putText(img, "My name is FR", (50, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (255, 51, 153), 3)
        cv2.putText(img, "Please Wait", (180, 420), cv2.FONT_HERSHEY_TRIPLEX, 2, (160, 255, 0), 2)
        f += 1
        if f == 1:
            num = num + 8
            f = 0
        cv2.line(img, (60, 500), (num, 500), (255, 255, 51), 50)
        cv2.putText(img, "...Running...", (240, 510), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 3)
        cv2.imshow('frame', img)
        k = cv2.waitKey(10)
        if num == 700:
            k = 25
            if k == 25:
                break
    cv2.destroyAllWindows()
    show_main()

def show_main():
    encodlistnow = findEncodings()
    cap = cv2.VideoCapture(0)
    cap.set(3, 1080)
    cap.set(4, 720)
    _, classname = file_name_pictures()
    s = 0
    second = 0
    ok = ""
    yes = ""
    text1 = ""
    textname = ""
    textage = ""
    textroot = ""
    know = "Do you know me?"
    butt_yes = ""
    xy1 = (0, 0)
    xy2 = (0, 0)
    xyt = (0, 0)
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgs = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
        Exit = "Exit"
        cv2.rectangle(frame, (70, 50), (450, 250), (153, 0, 153), -1)
        cv2.rectangle(frame, (70, 50), (450, 250), (0, 153, 0), 4)
        cv2.rectangle(frame, (70, 280), (250, 320), (153, 0, 153), -1)
        cv2.rectangle(frame, (70, 280), (250, 320), (0, 153, 0), 4)
        cv2.putText(frame, Exit, (130, 310), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        cv2.rectangle(frame, (270, 280), (450, 320), (153, 0, 153), -1)
        cv2.rectangle(frame, (270, 280), (450, 320), (0, 153, 0), 4)
        cv2.putText(frame, know, (285, 305), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        x = 100
        x1 = 285
        y = 290
        y1 = 305
        resulte = Hand.process(frameRGB)
        if resulte.multi_hand_landmarks:
            lm = find_hand(resulte.multi_hand_landmarks[0], w, h)
            cv2.circle(frame, lm[0], 4, (64, 64, 64), -1)
            if x<lm[0][0]<x+150 and y<lm[0][1]<y+30:
                cv2.rectangle(frame, (70, 280), (250, 320), (255, 0, 255), -1)
                cv2.putText(frame, Exit, (130, 310), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                s = s + 1
                if s == 15:
                    cv2.rectangle(frame, (70, 280), (250, 320), (0, 204, 0), -1)
                    os.close()
            if x1<lm[0][0]<x1+150 and y1<lm[0][1]<y1+30:
                cv2.rectangle(frame, (270, 280), (450, 320), (255, 0, 255), -1)
                cv2.putText(frame, know, (285, 305), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
                s = s + 1
                if s == 15:
                    cv2.rectangle(frame, (270, 280), (450, 320), (0, 204, 0), -1)
                    ok = ok + "ok"
                    s = 0
            if 450 < lm[0][0] < 450 + 100 and 160 < lm[0][1] < 160 + 50:
                cv2.rectangle(frame, xy1, xy2, (255, 0, 255), -1)
                cv2.putText(frame, butt_yes, xyt, cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                s = s + 1
                if s == 15:
                    cv2.rectangle(frame, xy1, xy2, (0, 204, 0), -1)
                    yes = yes + "yes"
                    s = 0
                    if yes == "yes":
                        F, L, A, G = GUI()
                        DB.add(str(F), str(L), str(A), str(G))
                        take_photo()
                        break
        if encodlistnow == []:
            text1 = "Initial setup..."
            textname = "I don't know no one"
            textage = "Would you like to "
            textroot = "introduce yourself to me?"
            xy1 = (470, 180)
            xy2 = (550, 220)
            xyt = (480, 210)
            butt_yes = "Yes"
        if ok == "ok":
            facecurframe = face_recognition.face_locations(imgs)
            encodcurframe = face_recognition.face_encodings(imgs, facecurframe)
            for encodface, faceloc in zip(encodcurframe, facecurframe):
                resultes = face_recognition.compare_faces(encodlistnow, encodface)
                facedis = face_recognition.face_distance(encodlistnow, encodface)
                matchindex = np.argmin(facedis)
                # print(resultes,matchindex)
                if resultes[matchindex]:
                    id = classname[matchindex]
                    fname, lname, age, gender = DB.show(id)
                    text1 = "Yes, your name is"
                    textname = f'{fname} {lname}'
                    textage = f"You are {age} years old"
                    if id == "1":
                        textroot = "You created me (root)"
                    else:
                        if gender == "M":
                            textroot = "You are a man"
                        else:
                            textroot = "You are a woman"
                else:
                    text1 = "No, I don't know you"
                    textname = "Would you like to "
                    textage = "introduce yourself to me?"
                    textroot = ""
                    xy1 = (470, 135)
                    xy2 = (550, 175)
                    xyt = (480, 165)
                    butt_yes = "Yes"
                    ok = ""
            s = s + 1
            if s == 20:
                s = 0
                ok = ""
        second = second + 1
        if second == 300:
            text1 = ""
            textname = ""
            textage = ""
            textroot = ""
            xy1 = (0, 0)
            xy2 = (0, 0)
            xyt = (0, 0)
            butt_yes = ""
            second = 0
        cv2.putText(frame, text1, (95, 85), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 1)
        cv2.putText(frame, textname, (95, 125), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 1)
        cv2.putText(frame, textage, (95, 165), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 1)
        cv2.putText(frame, textroot, (95, 205), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 1)
        cv2.rectangle(frame, xy1, xy2, (153, 0, 153), -1)
        cv2.rectangle(frame, xy1, xy2, (0, 153, 0), 4)
        cv2.putText(frame, butt_yes, xyt, cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        cv2.imshow('FR2', frame)
        k = cv2.waitKey(10)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def take_photo():
    cap = cv2.VideoCapture(0)
    FaceModel = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    SmileModel = cv2.CascadeClassifier('haarcascade_smile.xml')
    s = 0
    b = 0
    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        Faces = FaceModel.detectMultiScale(gray, 1.2, 10, minSize=(80, 80))
        cv2.putText(frame, "Please smile", (190, 40), cv2.FONT_HERSHEY_PLAIN, 3, (102, 0, 204), 2)
        name = creat_id()
        for face in Faces:
            x, y, w, h = face
            D_face = frame[y:y+h, x:x+w]
            D_face_gry = cv2.cvtColor(D_face, 6)
            take = frame[y-50:y+h+50, x-50:x+w+50]
            smiles = SmileModel.detectMultiScale(D_face_gry, 1.1, 10)
            for smile in smiles:
                _, _, _, _ = smile
                s = s + 1
                if s == 100:
                    f = os.getcwd()
                    os.chdir(f'{f}\\img')
                    cv2.imwrite(f'{str(name)}.jpg', take)
                    b = 27
        cv2.imshow('Take Photo', frame)
        k = cv2.waitKey(10)
        if k == 27 or b == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
DB()
show1()
#print(DB.show(1))