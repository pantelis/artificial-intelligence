# Segment Anything Model Finetuning for Remote Sensing Applications

![](images/impTile.png)

In this project you will be asked to segment sidewalks from satellite imagery. The importance of remote sensing and its associated job market is growing rapidly. Remote sensing powers, weather prediction, agriculture, urban planning, defense and many other applications. 

Lately, we have observed the advent of very large foundational models in NLP applications - sometimes these models result in  hundreds of billions of parameters - for example the [GPT-3](https://arxiv.org/abs/2005.14165) model that has 175 billion parameters. Can we do the same for computer vision applications ?  An example of a positive answer to this problem is the Segmenting Anything Model (SAM).  

## Background

![](images/sam.png)

Read and experiment with [the SAM implementation](https://segment-anything.com/) and [the SAM paper](https://arxiv.org/abs/2101.04703).


## Milestone 1: Get to know Geographical Information Systems (GIS) and set up your development environment

See [this tutorial](https://docs.qgis.org/3.34/en/docs/gentle_gis_introduction/index.html) that is best to be followed in a desktop installation of [QGIS](https://qgis.org/en/site/). 

Use the [example docker container](https://github.com/pantelis/artificial-intelligence) if you have access to a local NVIDIA GPU. Note that you need to do the project in Pytorch and you need to edit the `devcontainer.json` file to point to the right container for PyTorch.   

In addition to python scripts you will also need python notebooks to experiment and visualize the SAM model outputs as well as geospatial data. The suggested container ships with [Jupyter](https://jupyter.org/) and if you use [Google Colab](https://colab.research.google.com/) you are obviously using notebooks.  


## Milestone 2: Replicate SAM implementation for satellite imagery

The SAM implementation for remote sensing applications is based on [this package](https://samgeo.gishub.org/). Go over the following video and replicate the workflow in your environment for the imagery used by the author.    

```{eval-rst}
.. youtube:: YHA_-QMB8_U
   :width: 100%
   :height: 400
   :align: center
```

The notebook based environment makes it very easy to experiment with the SAM model and the workflow. 

This [desktop QGIS plugin](https://github.com/BjornNyberg/Geometric-Attributes-Toolbox/wiki/User-Guide#segment-anything-model) is also available to help you experiment with the SAM model.


## Milestone 3: Finetune the SAM model for the sidewalks dataset

Use the sidewalk dataset (this is currently being prepared and will be released soon) and finetune the SAM model for this dataset. Follow these instructions to do so. 

```{eval-rst}
.. youtube:: 83tnWs_YBRQ
   :width: 100%
   :height: 400
   :align: center
```

Use loss functions and segementation quality metrics that are suitable for roads and sidewalks. You can see [this reference for guidance](https://www.sciencedirect.com/science/article/pii/S1569843222003478).  Avoid going into a rabbit hole of developing your own metrics - there are many metrics that are suitable for this task and you just need to be aware of them and use them. Note that sidewalks are many times more difficult to segment than roads due to their narrow width and the fact that they are often occluded by trees and other objects.

These include: 

- [Intersection over Union](https://en.wikipedia.org/wiki/Jaccard_index)
- [Dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)
- [F1 score](https://en.wikipedia.org/wiki/F-score)

## Milesone 4: Hugging Face App and Video Demo

Using the reacticve app framework [Shiny for Python](https://shiny.posit.co/py/) and the [Hugging Face Shiny spaces](https://huggingface.co/docs/hub/en/spaces-sdks-docker-shiny) to create a web app that allows the user to upload an image of a tile and get the sidewalk segmentation. You can use [this dashboard](https://shiny.posit.co/py/templates/map-distance/) as a starting point.

Produce a 2min video showcasing the problem statement and your demo. The video can be uploaded to your Youtube channel or linked as an mp4 file in your Github repo. 












