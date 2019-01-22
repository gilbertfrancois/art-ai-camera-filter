from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import cv2
import numpy as np
from keras.models import load_model
import glob
from capture import VideoCaptureAsync

CAM_WIDTH = 640
CAM_HEIGHT = 480


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        ones = np.ones((128, 128, 3))[np.newaxis]
        print(ones.shape)
        model_path_list = glob.glob('../model/*.hdf5')

        print('[*] Loading {} models...'.format(len(model_path_list)))
        self.model_list = [load_model(model_path) for model_path in model_path_list]
        print('[*] Warming up the machines...')
        for model in self.model_list:
            _ = model.predict(ones)
        print('[*] {} models loaded'.format(len(self.model_list)))
        self.current_model = 1
        self.alpha = 0
        self.beta = 0.05
        self.img_buffer = np.zeros((CAM_HEIGHT, CAM_WIDTH)).astype(np.uint8)

        self.setupUi(self)
        # Connect button signal to appropriate slot
        # self.myButton.released.connect(self.myButtonPushed)
        self.start_webcam()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_webcam()

    def start_webcam(self):
        self.cap = VideoCaptureAsync(0, CAM_WIDTH, CAM_HEIGHT)
        self.cap.start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def stop_webcam(self):
        self.cap.stop()

    def update_frame(self):
        _, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1)
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = self.process_image(self.frame)
        self.display_frame()

    def process_image(self, src):
        self.alpha += 0.01
        if self.alpha > 1:
            self.alpha = 0
            self.current_model += 1
            if self.current_model >= len(self.model_list):
                self.current_model = 1

        # Edge detection
        img_edge = self.buffered_edge_detection(src)

        # Coloured image from ML models
        img_colors = self.feed_forward(src)

        # Compose layers
        img_blend = np.clip(((1 - self.beta) * (img_colors - img_edge * 0.1) + self.beta * self.frame).astype(np.uint8),
                            0, 255)

        # Blur for smooth effect
        dst = cv2.GaussianBlur(img_blend, (5, 5), cv2.BORDER_DEFAULT)
        return dst

    def buffered_edge_detection(self, src):
        org_image = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
        org_image = cv2.Canny(org_image, 100, 200)
        org_image = (0.8 * self.img_buffer + 0.2 * org_image).astype(np.uint8)
        self.img_buffer = org_image.copy()
        org_image = cv2.cvtColor(org_image, cv2.COLOR_GRAY2RGB)
        return org_image

    def feed_forward(self, src):
        src = cv2.resize(src, (128, 128), interpolation=cv2.INTER_CUBIC)
        X = src[np.newaxis]
        X = (X - np.min(X)) / (np.max(X) - np.min(X))
        X1 = self.predict(X, self.current_model)
        X2 = self.predict(X, self.current_model - 1)
        Xp = self.alpha * X1 + (1 - self.alpha) * X2
        Xp = (Xp * 255).astype(np.uint8)
        Xp = cv2.resize(Xp, (CAM_WIDTH, CAM_HEIGHT), interpolation=cv2.INTER_CUBIC)
        return Xp

    def predict(self, X, model_index):
        Xp = self.model_list[model_index].predict(X)[0]
        Xp = (Xp - np.min(Xp)) / (np.max(Xp) - np.min(Xp))
        return Xp

    def display_frame(self):
        image = QImage(
            self.frame,
            self.frame.shape[1],
            self.frame.shape[0],
            self.frame.shape[1] * 3,
            QImage.Format_RGB888
        )
        self.viewFinder.setPixmap(QPixmap.fromImage(image))
