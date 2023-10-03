import numpy as np
import cv2 as cv
import time


def create_scene(size):
    if size > 0:
        return np.zeros((size, size, 3), dtype="uint8")
    else:
        return np.zeros((10, 10, 3), dtype="uint8")


def destroy_scene():
    key = cv.waitKey(1) & 0xFF
    if key == 27 or key == ord("q") or cv.getWindowProperty('dark', cv.WND_PROP_AUTOSIZE) < 0:
        cv.destroyAllWindows()
        return True
    else:
        return False
