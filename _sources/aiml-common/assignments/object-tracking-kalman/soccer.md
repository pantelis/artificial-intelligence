# Sports Analytics - Object Tracking and Kalman Filters

Multi-Object Tracking (MOT) is a core visual ability that humans poses to perform kinetic tasks and coordinate other tasks. The AI community has recognized the importance of MOT via a series of [competitions](https://motchallenge.net). 

In this assignment, the object class is `person` and the ability to reason over time will be demonstrated using [Kalman Filters](https://en.wikipedia.org/wiki/Kalman_filter). The assignment will give you also the opportunity to apply probabilistixc reasoning to sports analytics (a sizable market for AI).

```{eval-rst}

.. youtube:: vUnuDTVHwGE

```

### Task 1: Deep-SORT (40 points)

Read [this](https://arxiv.org/abs/1602.00763) and [this](https://arxiv.org/abs/1703.07402) paper to understand the Deep-SORT algorithm. 

1. (10 poiints) Draw the architecture of the tracking solution using a diagraming tool of your choice that is compatible to Github rendering (excalidraw or diagrams.net or ...) 

2. (30 points) Write a summary of key components of the architecture above including the equations of the Kalman filter and explain what the Hungarian Algorithm will do . For the later you may benefit from going through [this](https://github.com/benchaplin/hungarian-algorithm) implementation.


### Task2: Deep-SORT Implementation (50 points)


Watch this video that explains the implementation of Deep-SORT:

```{eval-rst}

.. youtube:: sPu-V5Qy3CY

```

You are free to use [the code from the video](https://www.kaggle.com/code/sakshaymahna/deepsort) but you need to implement object detection based on [Faster-RCNN](https://pytorch.org/vision/main/models/faster_rcnn.html) and you also need to detect and track the soccer ball. Both `person` and `ball` are classes in the [COCO dataset](https://cocodataset.org/#home).

You will need to submit your video with all the bouding boxes of the players and the socker ball superposed on the test video below. 

```{eval-rst}

.. youtube:: l3NJNFmg09k

```

The test video results at the beginning of this page were generated using [this implementation](https://learnopencv.com/understanding-multiple-object-tracking-using-deepsort). You are free to also consult this code as well especially when it comes to the superposition part. 


### Task 3: Critique (10 points)

Comment on the inability of the Deep-SORT algorithm to handle unique identities of players.






