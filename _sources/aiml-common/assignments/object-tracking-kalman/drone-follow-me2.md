# Drone follow me using Kalman Filters

Multi-Object Tracking (MOT) is a core visual ability that humans poses to perform kinetic tasks and coordinate other tasks. The AI community has recognized the importance of MOT via a series of [competitions](https://motchallenge.net). 

In this assignment, the object class is `bicycle` and the ability to track this object  will be demonstrated using [Kalman Filters](https://en.wikipedia.org/wiki/Kalman_filter).  


## Task 1: Setup your development environment and store the test video locally (10 points)

```{eval-rst}
.. youtube:: 2hQx48U1L-Y
```
Your environment must be docker based and you can use any TF2 or PT2 based docker container compatible with your environment. You can also use colab. 

## Task 2: Object Detection (40 points)

Split the videos into frames and use an object detector of your choice, in a framework of your choice to detect the cyclists.  

## Task 3: Kalman Filter (50 points)

Use the  [filterpy](https://filterpy.readthedocs.io/en/latest/kalman/KalmanFilter.html) library to implement Kalman filters that will track the cyclists in the video. You will need to use the detections from the previous task to initialize the Kalman filter. 

You need to deliver a video that contains the trajectory of the cyclists as a line that connects the pixels that the tracker indicated. This means that the trajectory will have no gaps as the cyclists are occluded from the field of view. You can use the `ffmpeg` command line tool and OpenCV to superpose the bounding box of the drone on the video as well as plot its trajectory. 

You will need to employ multiple Kalman filters to track an equal number of cyclists. The trajectories should never intersect indicating that the tracker confused the tracked cyclist with the other cyclist. 
