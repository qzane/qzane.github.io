---
layout: post
title: 3D Scene Reconstruction of A Single Monocular Photos by Estimating the Orientation of Rectangles
---

# Demo
![Demo](/images/161208-3d-reconstruction-mix.jpg "Demo")  <br>
(No.15 showed an error due to low photo resoluction) <br>
![3D Scene Reconstruction](/images/161208-3d-reconstruction-3.gif "3D Scene Reconstruction")  <br>

# Description 
This is just part of my undergraduate thesis about "Scene Understanding for Robots" which is still under constrction, so that this post may seem unfinished. I'm sorry for that, but you are always welcomed to contact me[AT]qzane.com for details if you are interested.

## Original Photo(Perspective projection)
## Finding Strong Outlines and Potential Rectangles (Perspective projection)
This is actually a critical section of this task, and I'm currently using some empirical methods to find potential spacial rectangles like using the completeness of angles formed between lines. However the result is not that good and I am trying some new models with the help of [NYU Depth Dataset V2](http://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) and [Stanford 2D-3D-Semantics Dataset](http://buildingparser.stanford.edu/dataset.html). <br>

Questions and suggestions by email are always welcomed!

## Surface Oriantation Estimation(Perspective projection)
Detailed reasoning process can be downloaded [here](https://github.com/qzane/qzane.github.io/raw/master/attachments/161208-calculate-orientation-rectangles.pdf "calculate-orientation-rectangles.pdf"). The following is an outline. <br>
![Notations](/images/161208-3d-reconstruction-notation.png "Notations") <br>
As shown in the picture above. ![tex](https://latex.codecogs.com/gif.latex?O) is the optical center of the camera and ![tex](https://latex.codecogs.com/gif.latex?\vec&space;z_1) is its optical axis. ![tex](https://latex.codecogs.com/gif.latex?O_{xyz}) is a 3D orthogonal coordinate system and ![tex](https://latex.codecogs.com/gif.latex?O_0-uv) is the image plane with ![tex](https://latex.codecogs.com/gif.latex?OO) as its image center. <br>

we are going to estimate the oriantation of the ![tex](https://latex.codecogs.com/gif.latex?plane(P_1-P_4)), or more specifically: its normal vector ![tex](https://latex.codecogs.com/gif.latex?\vec&space;V), with its projection ![tex](https://latex.codecogs.com/gif.latex?PP_1-PP_4) on the image plane.  <br>

The problem can be reduce to find the value of ![tex](https://latex.codecogs.com/gif.latex?Z_2) which can minimal the value of our object function: <br>
![object function](/images/161208-3d-reconstruction-objFunction.png "object function") <br>

where <br>
![variables](/images/161208-3d-reconstruction-vars.png "variables") <br>

![tex](https://latex.codecogs.com/gif.latex?Z_1=300) (or any other constant, all of which will lead to the same result of ![tex](https://latex.codecogs.com/gif.latex?\vec&space;V)) <br>

Since our object function has only one variable(![tex](https://latex.codecogs.com/gif.latex?Z_2)), there are dozens of methods to find its minimal, I tried particle swarm optimization (PSO), and it worked well. <br>


Once we get the value of ![tex](https://latex.codecogs.com/gif.latex?Z_2), we get the value of ![tex](https://latex.codecogs.com/gif.latex?P_1-P_4), with which, we can calculate the value of ![tex](https://latex.codecogs.com/gif.latex?\vec&space;V) easily. <br>

## 3D Scene Reconstruction(Orthographic projection)

Once we have the oriantations of all rectangles, we can infer their relative positions from the intersections in the photo and eventually reconstruct the whole scene. Although the low resoluction and some potential distortion in the photo may cause some error, they won’t have large impact to the whole model because the oriantations are calculated independently. <br>

# Experimental Results
I’m currently trying to do some qualitative analysis using [NYU Depth Dataset V2](http://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) and [Stanford 2D-3D-Semantics Dataset](http://buildingparser.stanford.edu/dataset.html). I will also compare my result with some other works and update the results here. Email me if you are interested about current results.
