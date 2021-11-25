import ntpath
import os.path

from django.shortcuts import render, redirect
import cv2
from pathlib import Path


# Create your views here.

def index(request):
    return render(request, 'index.html')

def erro(request):
    return render(request, 'erro.html')

def ativar_camera(request):
    try:

        face_detector = cv2.CascadeClassifier(str(os.path.abspath('media/haarcascade_frontalface_default.xml')))

        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            detections = face_detector.detectMultiScale(image_gray, minSize=(100, 100), minNeighbors=5)
            aspaoskapok
            # Draw a rectangle around the faces
            for (x, y, w, h) in detections:
                print(w, h)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            cv2.putText(frame, 'Clique a letra Q para sair!', (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (255, 255, 0))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
        return redirect('index')

    except:

        return redirect('erro')
