import cv2
import torch
import time

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = 0.4  # confidence threshold

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        start = time.time()
        results = model(frame)
        annotated = results.render()[0]
        fps = 1 / (time.time() - start)
        cv2.putText(annotated, f"FPS: {fps:.2f}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Traffic Detection', annotated)
        if cv2.waitKey(1) == 27:  # ESC to quit
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video("data/sample_videos/intersection.mp4")
