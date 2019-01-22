import threading
import cv2

class VideoCaptureAsync(threading.Thread):
    def __init__(self, src=0, width=640, height=480):
        super().__init__()
        self.daemon = True
        self.setName('VideoCapture')
        self.src = src
        self.cap = cv2.VideoCapture(self.src)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.grabbed, self.frame = self.cap.read()
        self.running = False
        self.read_lock = threading.Lock()

    def set(self, var1, var2):
        self.cap.set(var1, var2)

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        super().start()

    def run(self):
        while self.running:
            grabbed, frame = self.cap.read()
            if frame is not None:
                with self.read_lock:
                    self.frame = frame
                    self.grabbed = grabbed

    def read(self):
        with self.read_lock:
            frame = self.frame.copy()
            grabbed = self.grabbed
        return grabbed, frame

    def __exit__(self, exec_type, exc_value, traceback):
        self.cap.release()


if __name__ == '__main__':
    cap = VideoCaptureAsync(0, 640, 480)
    cap.start()
    for i in range(1000):
        grabbed, frame = cap.read()
        cv2.imshow('test', frame)
        cv2.waitKey(1)
    cap.stop()
    cap.join()
