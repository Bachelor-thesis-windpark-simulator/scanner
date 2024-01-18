import cv2
import uuid

def capture_and_save_image():
    # Video-Capture-Objekt erstellen (0 für die Standardkamera)
    cap = cv2.VideoCapture(0)

    # Warten, bis die Kamera bereit ist
    while True:
        ret, frame = cap.read()
        if ret:
            break

    while True:
        # Video-Live-Feed anzeigen
        cv2.imshow('Press Space to Capture, Press ESC to Quit', frame)

        # Warten auf Benutzereingabe
        key = cv2.waitKey(1) & 0xFF

        # Wenn Leertaste gedrückt wird, ein Bild erfassen
        if key == ord(' '):
            # Eindeutige ID für das Bild generieren
            image_id = str(uuid.uuid4())

            # Bild speichern
            image_path = f"bilder/{image_id}.png"
            cv2.imwrite(image_path, frame)

            print(f"Image captured and saved with ID: {image_id}")

        # Video-Capture-Objekt für das nächste Frame aktualisieren
        ret, frame = cap.read()

        # Wenn ESC gedrückt wird, das Programm beenden
        if key == 27:  # 27 entspricht der Escape-Taste
            break

    # Video-Capture-Objekt und Fenster freigeben
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_save_image()
