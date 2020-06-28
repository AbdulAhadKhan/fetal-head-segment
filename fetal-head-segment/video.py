import cv2
from utils import save_image
from predict import Predictor
from __main__ import __file__

class Video:
    def __init__(self, video_path, predictor_settings,
                 save=False, save_dir=None):
        self.video = self._load_video(video_path)
        self.save = save
        self.save_dir = save_dir
        self.predictor = Predictor(**predictor_settings)

    @staticmethod
    def _load_video(video_path):
        return cv2.VideoCapture(video_path)

    def stream(self):
        frame_no = 1
        fps = self._get_frame_rate()
        while self.video.isOpened():
            frame = self.video.read()[1]
            frame = self.predictor.process_image(frame)
            if self.predictor.image_class == 'Head' and self.save:
                save_image(frame, f'{self.save_dir}/{frame_no}.png')
            cv2.imshow(__file__, frame)
            if cv2.waitKey(fps) & 0xFF is ord('q'):
                break

    def _get_frame_rate(self):
        fps = self.video.get(cv2.CAP_PROP_FPS)
        return int(fps)
