# Multiple Object Tracking

Multi-Object Tracking (MOT) is a core visual ability that humans poses to perform kinetic tasks and coordinate other tasks. The AI community has recognized the importance of MOT via a series of [competitions](https://motchallenge.net). 

 The ability to reason even in the absence of perception input task was highlighted in Lecture 1 using a document camera and a canopy type of occlusion where an object moves below it. In this assignment, the object class is `ball` and the ability to reason over time will be demonstrated using [Kalman Filters](https://en.wikipedia.org/wiki/Kalman_filter). There will be two cases of occlusion: occlusion by a different object and occlusion by the same object (typical case of the later is on tracking people in crowds). 

## Task 1: Understand the problem and setup environment (20 points)

The problem is best described using this explanatory video below of the raw source files of this assignment:

1. [Single object tracking](https://github.com/sseshadr/auvsi-cv-all/blob/master/objectTracking/examples/ball.mp4)
2. [Multi-object tracking](https://github.com/sseshadr/auvsi-cv-all/blob/master/objectTracking/examples/multiObject.avi)

```{eval-rst}
.. youtube:: 0jAC9sMQQuM
```

The associated to the video github is [here](https://github.com/sseshadr/auvsi-cv-all). 

## Task 2: Object Detector (40 points)

In this task you will use a CNN-based object detector to bound box all `ball` instances in each frame. Because the educational value is  not object detection, you are allowed to use an object detector of your choice trained to distinguish the `ball` class. You are free to use a pre-trained model (eg on MS COCO that contains the class `sports ball` or train a model yourself.  Ensure that you explain thoroughly the code. 


## Task 3: Tracker (40 points)

The detector outputs can be used to obtain the centroid(s) of the `ball` instances across time. You can assign a suitable starting state in the 1st frame of the video and obtain the predicted trajectory of the object during both visible and occluded frames. You need to superpose your predicted position of the object in each frame and the raw frame and store a sequence of all frames (generate a video).  Ensure that you explain thoroughly the code. 

```{note}
You can use OpenCV (`import cv2`) for only the satellite parts of this assignment - Use numpy, or better, jax to code the Kalman filter. You need to submit the assignment either as a notebook URL or a Github URL. 
```
