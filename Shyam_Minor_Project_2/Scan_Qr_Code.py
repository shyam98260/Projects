import cv2
from pyzbar.pyzbar import decode
import numpy as np

def scan():
    def barcodeReader(image, bgr):
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        barcodes = decode(gray_img)

        for decodedObject in barcodes:
            points = decodedObject.polygon

            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        cv2.putText(frame, 'Press Q For Exit', (30, 440), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                    (0, 255, 0), 4)
        for bc in barcodes:
            cv2.putText(frame, bc.data.decode("utf-8") + " - " + bc.type, (30, 30),cv2.FONT_HERSHEY_SIMPLEX, 1,bgr, 2)
            return bc.data.decode("utf-8")

    bgr = (8, 70, 208)
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    ok = True
    while ok:
        ret, frame = cap.read()
        barcode = barcodeReader(frame, bgr)
        if barcode != None:
            ok=False
            cap.release()
            cv2.destroyAllWindows()
            return barcode
        cv2.imshow('Barcode reader', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break

if __name__=="__main__":
    print(showerror('ShowError', 'Please Run the Login.py First to access all the services'))
    exit(0)