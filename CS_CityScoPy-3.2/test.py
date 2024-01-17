import cv2
import numpy as np

# Definieren Sie Ihre Matrix und Verzerrungskoeffizienten
matrix =  [[1.38767649e+03, 0.00000000e+00, 9.51126861e+02],[0.00000000e+00, 1.38951691e+03, 4.55250696e+02],[0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]
distortion = [[-3.75450783e-01,  2.05276702e-01, -5.78245580e-04,  9.27857525e-06, -6.47422703e-02]]

# Konvertieren Sie sie in numpy Arrays
camera_matrix = np.array(matrix)
distortion_coefficients = np.array(distortion)

# Öffnen Sie die Kamera
cap = cv2.VideoCapture(0)

while True:
    # Lesen Sie das Bild von der Kamera
    ret, frame = cap.read()

    if ret:
        # Entzerren Sie das Bild
        h, w = frame.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficients, (w,h), 1, (w,h))

        # Entzerren
        dst = cv2.undistort(frame, camera_matrix, distortion_coefficients, None, newcameramtx)

        # Schneiden Sie das Bild auf die ROI
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]

        # Zeigen Sie das entzerrte Bild an
        cv2.imshow('Entzerrtes Bild', dst)

    # Beenden Sie die Schleife, wenn die 'q' Taste gedrückt wird
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Schließen Sie das Fenster und geben Sie die Kamera frei
cap.release()
cv2.destroyAllWindows()