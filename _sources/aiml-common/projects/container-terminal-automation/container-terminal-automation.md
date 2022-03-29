# Omniverse Container Terminal Oracle Network 


![](images/port.png)

In the last few years the industry of global logistics has been elevated to a _mission critical_ status.  One of the main areas that urgently requires improvement, especially in the US, is [Container Terminal Automation](https://www.elementai.com/news/2019/ai-and-the-future-of-port-automation). 

```{eval-rst}
.. youtube:: HkauiGYT6YY
```

In addition, the area of insuring supply chains, is posed for a shakeup as blockchain powered smart contracts are [disrupting the supply chain](https://blog.chain.link/blockchain-insurance/)

In this project you will have the opportunity to study the world modeling ability of integrating perception and AI modeling of a smart port that is offering data feeds to oracle networks. 

```{eval-rst}
.. youtube:: HiuvsLNCg-Y
```

This project is a PoC that offers the following features to the problem of automating the state update of digital twins from sensing and prognosticating smart contract off-network data. 


## Step 1: Setup

The environment that will be used for modeling of a smart port is Omniverse. Each student must use an RTX card and an Ubuntu OS (duel boot VM or any GPU passthrough is OK).  Consult [this repo](https://github.com/pantelis-classes/omniverse-ai) for the setup. 


## Step 2: Virtual World (Scene)

Create a simple world that consists of a flat docking area and several objects of interest eg 3D models of containers. It is OK to use simpler 3D objects such as [shipping boxes](https://medium.com/@ringlayer/cardboard-box-detection-using-retinanet-keras-5d4f331d9d15). 


## Step 3: Connect a real camera To Isaac 

You can connect natively or via the ROS2 Bridge.  Any document camera or webcam or IP camera will be sufficient for this task. At the end of this task the video frames are captured by IsaaC. 

## Step 3 alternative: Virtual camera

You can create a virtual camera that will oversee the 3D scene with the objects you created in step 2.

## Step 4: Learn to detect the objects 

In the case of 3D models of shipping containers this is largely a replication of [learning in simulated worlds](https://github.com/pantelis-classes/omniverse-ai). In the case of boxes you need to train a network that will detect them - the dataset is already available. 

## Step 5: Digital Twin Update

In this step you need to show how a real world physical movement of a real object can update the digital twin of the object in IsaaC. You are free to use markers to detect the relative location of the physical object.  

## Step 5 alternative: Digital Twin Update

In this step you write a Python script that can change the location or the number of objects you have in the scene. 

## Step 6: Smart Contract 

You use the Chainlink APIs to author a smart contract that will consume the stream representing the state of the scene and initiate a payment the moment the IsaaC scene reaches a desired state. The desired state is either a movement of the virtual object or the presence of N objects in the scene. 

