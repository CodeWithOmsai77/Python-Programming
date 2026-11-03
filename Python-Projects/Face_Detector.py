
import cv2
import time


def main():

    # Load OpenCV pre-trained Haar Cascade face detector
    cascade_path = (
        cv2.data.haarcascades
        + "haarcascade_frontalface_default.xml"
    )

    face_detector = cv2.CascadeClassifier(cascade_path)

    if face_detector.empty():
        print("Error: Could not load face detection model.")
        return

    # Open webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not access webcam.")
        return

    # Set webcam resolution
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("Advanced Face Detection Started")
    print("Press Q to exit.")

    previous_time = time.perf_counter()

    try:
        while True:

            # Capture webcam frame
            success, frame = camera.read()

            if not success:
                print("Error: Could not read webcam frame.")
                break

            # Convert frame to grayscale
            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            # Reduce image noise while preserving edges
            gray = cv2.bilateralFilter(
                gray,
                5,
                50,
                50
            )

            # Improve image contrast
            gray = cv2.equalizeHist(gray)

            # Detect faces
            faces = face_detector.detectMultiScale(
                gray,
                scaleFactor=1.05,
                minNeighbors=6,
                minSize=(40, 40),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # Draw bounding boxes
            for (x, y, w, h) in faces:

                # Green rectangle
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                # Face label background
                cv2.rectangle(
                    frame,
                    (x, max(0, y - 30)),
                    (x + w, y),
                    (0, 255, 0),
                    -1
                )

                # Face label
                cv2.putText(
                    frame,
                    "FACE DETECTED",
                    (x + 5, max(20, y - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    (0, 0, 0),
                    2
                )

            # Count detected faces
            face_count = len(faces)

            # Calculate FPS
            current_time = time.perf_counter()

            elapsed = current_time - previous_time

            fps = 1 / elapsed if elapsed > 0 else 0

            previous_time = current_time

            # Display face count
            cv2.putText(
                frame,
                f"Faces Detected: {face_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

            # Display FPS
            cv2.putText(
                frame,
                f"FPS: {fps:.1f}",
                (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2
            )

            # Display webcam output
            cv2.imshow(
                "Advanced Real-Time Face Detection",
                frame
            )

            # Exit using Q
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:

        # Release resources
        camera.release()
        cv2.destroyAllWindows()

        print("Face Detection Stopped")


if __name__ == "__main__":
    main()
