# Visual Prompting and Oclusion Handling for Remote Sensing Applications

## Milestones 1-4

These are described in the SAM Finetuning project. 

## Milestone 5: Occlusion Handling with Visual Prompting

[Visual Prompting](https://landing.ai/blog/what-is-visual-prompting/) has been shown to improve the performance of segmentation models. SAM is able to accommodate multiple modalities for prompting, either visual or natural language text and [this paper](https://kychen.me/RSPrompter/) shows that the right prompting can significantly outperform earlier schemes that used dedicated detectors as opposed to the more recent pretrained approaches.  Although the SAM model has been shown with finetuning to be able to do a reasonable job at segmenting features in remote sensing applications, it is still unable to handle occlusions. Occlusions create havoc in semantic segmentation of sidewalks and other small features. 

In this milestone you will address this problem through prompting. You will introduce a class called tree and use the visual prompting capability of SAM to prompt the model in such a way that you can segment the occluded sidewalk segments.

**Effectively you need to use a prompt to encode the information that the sidewalk did not stop at the tree but continues under it.**

Write the `SidewalkPrompter` that can automate the prompting into the SAM model for the sidewalk finetuning dataset. If you use a visual prompring only, given a set of points, two on each side of the tree segmentation and one or more centered on the tree(s) segmentation, the `SidewalkPrompter` should result into merging the two sidewalk segments as shown in the figure below.

![](images/r3.png)

You are free also to use [LangSAM](https://github.com/luca-medeiros/lang-segment-anything) as shown [here](https://samgeo.gishub.org/examples/text_prompts_batch/) in combination with the visual prompting to address the occlusion problem. 

The `SidewalkPrompter` can include other than prompt logic, the end result being the  stitching of the separated sidewalks segments for all occlusion events in the dataset.

You deliver how your implementation can correct 10 test dataset images that exhibit erroneous segmentations due to occlusion.  Showcase your woork showing the result before and after occlusion handling. 


```{note}
You can continue on this task after the course ends by rolling the visual prompting capability into the open source tool [CVAT](cvat.ai) allowing anyone to use the visual prompts for accelerating annotation work.  
```
