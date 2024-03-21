# Drone follow me using Kalman Filters

Multi-Object Tracking (MOT) is a core visual ability that humans poses to perform kinetic tasks and coordinate other tasks. The AI community has recognized the importance of MOT via a series of [competitions](https://motchallenge.net). 

In this assignment, the object class is `bicycle` and `car` the ability to track these objects  will be demonstrated using [Kalman Filters](https://en.wikipedia.org/wiki/Kalman_filter).  


## Task 1: Setup your development environment and store the test video locally (10 points)

Your environment must be docker based and you can use any TF2 or PT2 based docker container compatible with your environment. You can also use colab. 

## Task 2: Object Detection (40 points)

Perform object detection on the following videos. 

```{eval-rst}
.. youtube:: WeF4wpw7w9k
```

```{eval-rst}
.. youtube:: 2NFwY15tRtA
```

```{eval-rst}
.. youtube:: 5dRramZVu2Q
```

Split the videos into frames and use an object detector of your choice, in a framework of your choice to detect the cyclists.  

## Task 3: Kalman Filter (50 points)

Use the  [filterpy](https://filterpy.readthedocs.io/en/latest/kalman/KalmanFilter.html) library to implement Kalman filters that will track the cyclist and the vehicle (if present) in the video. You will need to use the detections from the previous task to initialize and run the Kalman filter. 

You need to deliver a video that contains the trajectory of the objects as a line that connects the pixels that the tracker indicated. You can use the `ffmpeg` command line tool and OpenCV to superpose the bounding box of the drone on the video as well as plot its trajectory. 

Suggest methods that you can use to address  false positives and how the tracker can help you in this regard.

You will need to have one Kalman filter to track each of the required and present objects (cyclist and vehicle).


## Extra Bonus (20 points)

```{eval-rst}
.. youtube:: 2hQx48U1L-Y
```

The cyclist in the video goes in and out of occlusions. In addition the object is small making detections fairly problematic without finetuning and other optimizations.  Fintetuning involves using the pretrained model and training it further using images of cyclists from a training dataset such as [VisDrone](https://github.com/VisDrone/VisDrone-Dataset). At the same time,  reducing the number of classes to a much smaller number such as person & bicycle may help.  Also some 2 stage detectors may need to be further optimized in terms of parameters for small objects. See [this paper](https://www.mdpi.com/1424-8220/23/15/6887) for ideas around small object tracking. 


```{note}
The extra points can only be awarded in the category of `assignments` and cannot be used to compensate for any other category such as `exams`. 
```

