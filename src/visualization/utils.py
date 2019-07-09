import cv2
import matplotlib
import numpy as np


colors = list(matplotlib.colors.cnames.values())

hex_to_rgb = lambda h: tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
colors = [hex_to_rgb(x[1:]) for x in colors]
colors = [(255, 0, 0)] + colors

def draw_faces_with_keypoints(im, bboxes, keypoints, draw_bboxes=True):
    radius = max(int(max(im.shape)*0.0025), 1)
    for c_idx, (bbox, keypoint) in enumerate(zip(bboxes, keypoints)):
        color = colors[c_idx % len(colors)]
        x0, y0, x1, y1 = bbox
        if draw_bboxes:
            im = cv2.rectangle(im, (x0, y0), (x1, y1), color)
        for (x,y) in keypoint:
            im = cv2.circle(im, (x,y), radius, color)

    if type(im) != np.ndarray:
        return im.get()
    return im