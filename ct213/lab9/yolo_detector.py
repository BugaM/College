from tensorflow.keras.models import load_model
import cv2
import numpy as np
from utils import sigmoid


class YoloDetector:
    """
    Represents an object detector for robot soccer based on the YOLO algorithm.
    """
    def __init__(self, model_name, anchor_box_ball=(5, 5), anchor_box_post=(2, 5)):
        """
        Constructs an object detector for robot soccer based on the YOLO algorithm.

        :param model_name: name of the neural network model which will be loaded.
        :type model_name: str.
        :param anchor_box_ball: dimensions of the anchor box used for the ball.
        :type anchor_box_ball: bidimensional tuple.
        :param anchor_box_post: dimensions of the anchor box used for the goal post.
        :type anchor_box_post: bidimensional tuple.
        """
        self.network = load_model(model_name + '.hdf5')
        self.network.summary()  # prints the neural network summary
        self.anchor_box_ball = anchor_box_ball
        self.anchor_box_post = anchor_box_post

    def detect(self, image):
        """
        Detects robot soccer's objects given the robot's camera image.

        :param image: image from the robot camera in 640x480 resolution and RGB color space.
        :type image: OpenCV's image.
        :return: (ball_detection, post1_detection, post2_detection), where each detection is given
                by a 5-dimensional tuple: (probability, x, y, width, height).
        :rtype: 3-dimensional tuple of 5-dimensional tuples.
        """
        image = self.preprocess_image(image)
        output = self.network.predict(image)
        output = self.process_yolo_output(output)
        return output

    def preprocess_image(self, image):
        """
        Preprocesses the camera image to adapt it to the neural network.

        :param image: image from the robot camera in 640x480 resolution and RGB color space.
        :type image: OpenCV's image.
        :return: image suitable for use in the neural network.
        :rtype: NumPy 4-dimensional array with dimensions (1, 120, 160, 3).
        """
        width = 160
        height = 120
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        image = np.array(image)
        image = image/255.0
        image = np.reshape(image, (1, 120, 160, 3))
        return image

    def process_yolo_output(self, output):
        """
        Processes the neural network's output to yield the detections.

        :param output: neural network's output.
        :type output: NumPy 4-dimensional array with dimensions (1, 15, 20, 10).
        :return: (ball_detection, post1_detection, post2_detection), where each detection is given
                by a 5-dimensional tuple: (probability, x, y, width, height).
        :rtype: 3-dimensional tuple of 5-dimensional tuples.
        """
        coord_scale = 4 * 8  # coordinate scale used for computing the x and y coordinates of the BB's center
        bb_scale = 640  # bounding box scale used for computing width and height
        pwb = 5
        phb = 5
        pwp = 2
        php = 5
        output = np.reshape(output, (15, 20, 10))  # reshaping to remove the first dimension

        tb = output[:, :, 0]

        pb = sigmoid(tb)
        max_pb = np.max(pb)
        index = np.where(pb == max_pb)
        cell = output[index[0], index[1], :].flatten()
        txb = cell[1]
        tyb = cell[2]
        twb = cell[3]
        thb = cell[4]

        xb = (index[1] + sigmoid(txb)) * coord_scale
        yb = (index[0] + sigmoid(tyb)) * coord_scale
        wb = bb_scale * pwb * np.exp(twb)
        hb = bb_scale * phb * np.exp(thb)

        tp = output[:, :, 5]
        pp = sigmoid(tp)
        max_pp1 = np.max(pp)
        index = np.where(pp == max_pp1)
        cell = output[index[0], index[1], :].flatten()
        txp1 = cell[6]
        typ1 = cell[7]
        twp1 = cell[8]
        thp1 = cell[9]

        xp1 = (index[1] + sigmoid(txp1)) * coord_scale
        yp1 = (index[0] + sigmoid(typ1)) * coord_scale
        wp1 = bb_scale * pwp * np.exp(twp1)
        hp1 = bb_scale * php * np.exp(thp1)

        pp[index] = -1
        max_pp2 = np.max(pp)
        index = np.where(pp == max_pp2)
        cell = output[index[0], index[1], :].flatten()
        txp2 = cell[6]
        typ2 = cell[7]
        twp2 = cell[8]
        thp2 = cell[9]

        xp2 = (index[1] + sigmoid(txp2)) * coord_scale
        yp2 = (index[0] + sigmoid(typ2)) * coord_scale
        wp2 = bb_scale * pwp * np.exp(twp2)
        hp2 = bb_scale * php * np.exp(thp2)

        ball_detection = (max_pb, xb, yb, wb, hb)
        post1_detection = (max_pp1, xp1, yp1, wp1, hp1)
        post2_detection = (max_pp2, xp2, yp2, wp2, hp2)
        return ball_detection, post1_detection, post2_detection
