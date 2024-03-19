# Visual Prompting and Oclusion Handling for Remote Sensing Applications

## Milestones 1, 2 & 3 

These are described in the SAM Finetuning project. 

Do **one** of the two milestones below. 

## Milestone 5a: Visual Prompting

[Visual Prompting](https://landing.ai/blog/what-is-visual-prompting/) has been shown to improve the performance of segmentation models.

[This paper](https://kychen.me/RSPrompter/) implements visual prompting for the SAM model and remote sensing applications. 

```{note}
You can continue on this task after the course ends by rolling the visual prompting capability into the open source tool [CVAT](cvat.ai) allowing anyone to use the visual prompts for accelerating annotation work.  
```

## Milestone 5b: Occlusions and Shadows

Occlusions create havoc in semanatic segmentation of sidewalks and other small features. 

![](images/r3.png)

Provide experiental evidence and commentary that address **one** of the following research opportunities provided below without any particular order.  

1. Consider the fact that sidewalk are 99.99% next to a road / street. How can we use this information, the segmentations of other features such as trees / vegetation and scene graphs to suggest that two segements interrupted by an occlusion can be connected ? 

2. Consider a hypothetical pedestrian with a simple mobility model walking on a sidewalk segment. Can we use a Hidden Markov Model (HMM) to predict their trajectory and connect the two sidewalk segments ?  

3. Consider that we have the segmentations of trees / folliage. Can we treat those as corruptions and use inpainting to fill in the occluded sidewalk segments, effectively creating a two step process for segmenting sidewalks ? 

```{note}
You can continue on this task after the course ends by considering additional ideas such as correspondence learning. Bringing in segmentations from streetview imagery at points of occlusion and reprojecting the lines. 
```
