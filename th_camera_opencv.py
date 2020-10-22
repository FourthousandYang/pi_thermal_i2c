import os
import cv2
from pylepton import Lepton
from th_base_camera import ThBaseCamera


class ThCamera(ThBaseCamera):
    #video_source = 0

    def __init__(self):
        super(ThCamera, self).__init__()

    

    @staticmethod
    def frames():
        

        # getImage = a.copy()
        # if not camera.isOpened():
        #     raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            
            with Lepton() as l:
                a,_ = l.capture()

            a = cv2.resize(a[:,:], (640, 480))
            # encode as a jpeg image and return it
            yield a#cv2.imencode('.jpg', img)[1].tobytes()
