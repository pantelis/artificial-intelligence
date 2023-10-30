# UAV Detection and Tracking

Multi-Object Tracking (MOT) is a core visual ability that humans poses to perform kinetic tasks and coordinate other tasks. The AI community has recognized the importance of MOT via a series of [competitions](https://motchallenge.net). 

In this assignment, the object class is `drone` and the ability to track this object  will be demonstrated using [Kalman Filters](https://en.wikipedia.org/wiki/Kalman_filter). The assignment will give you the opportunity to apply probabilistic reasoning in the physical security application space. 


## Task 1: Setup your development environment and store the test videos locally (10 points)

```{eval-rst}

.. youtube:: DhmZ6W1UAv4

```

```{eval-rst}

.. youtube:: YrydHPwRelI

```

## Task 1: Drone Object Detection (40 points)

You need to research can use any dataset that can be used to detect the class `drone` such as the drones used for the test videos. Please be careful to distinguish between the datasets that detect objects *from* drones to datasets that detect *the* drones. Your object detector must use a deep learning model but you can use an existing object detector model architecture. 

Split the videos into frames and use each frame to present the drone detections you got. Store all images that you had detections in a folder called `detections`. Write your code in such a way that a number of videos can be processed from a directory and not just these two.


## Task 2: Kalman Filter (50 points)

Use the  `filterpy`` library to implement a Kalman filter that will track the drone in the video. You will need to use the detections from the previous task to initialize the Kalman filter. 

You need to deliver a number of short videos with each video containing **only** the frames where the drone is present in the test video and its 2D trajectory shown as a line that connects the pixels that the tracker indicated. You can use the `ffmpeg` command line tool and OpenCV to superpose the bounding box of the drone on the video as well as plot its trajectory. 
