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
        dims = self._get_dims()
        while self.video.isOpened():
            frame = self.video.read()[1]
            frame = self.predictor.process_image(frame)
            if self.predictor.image_class == 'Head' and self.save:
                save_image(frame, f'{self.save_dir}/{frame_no}.png')
            frame = cv2.resize(frame, dims, cv2.INTER_NEAREST)
            frame = self._embed_class(frame)
            cv2.imshow(__file__, frame)
            if cv2.waitKey(fps) & 0xFF is ord('q'):
                break

    def _get_frame_rate(self):
        fps = self.video.get(cv2.CAP_PROP_FPS)
        return int(fps)

    def _get_dims(self):
        height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        return int(width), int(height)

    def _embed_class(self, frame):
        image = cv2.putText(frame, self.predictor.image_class,
                            (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                            1, (0, 0, 255), 1, cv2.LINE_AA)
        return image
