---
layout: post
title: 3D Scene Reconstruction of A Single Monocular Photos by Estimating the Orientation of Rectangles
---
This is just part of my undergraduate thesis about "Scene Understanding for Robots" which is still under constrction, so that this post may seem unfinished. I'm sorry for that, but you are always welcomed to contact me[AT]qzane.com for details if you are interested.

# Demo
Original Photo(Perspective projection)  <br>
![Original Photo](/images/161208-3d-reconstruction-0.BMP "Original Photo")  <br>
Strong Outlines(Perspective projection)  <br>
![Strong Outlines](/images/161208-3d-reconstruction-1.bmp "Strong Outlines")  <br>
Surface Oriantation Estimation(Perspective projection)  <br>
![Surface Oriantation Estimation](/images/161208-3d-reconstruction-2.bmp "Surface Oriantation Estimation")  <br>
3D Scene Reconstruction(Orthographic projection)  (No.15 showed an error due to low photo resoluction) <br>
![3D Scene Reconstruction](/images/161208-3d-reconstruction-3.gif "3D Scene Reconstruction")  <br>

# Description 
## Original Photo(Perspective projection)
## Finding Strong Outlines and Potential Rectangles (Perspective projection)
I’m still trying different methods to find rectangles more precisely, and I'm trying to make use of [NYU Depth Dataset V2](http://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) as my training set. <br>
Questions and suggestions by email are always welcomed!

## Surface Oriantation Estimation(Perspective projection)
Detailded reasoning process can be download [here](https://github.com/qzane/qzane.github.io/raw/master/attachments/161208-calculate-orientation-rectangles.pdf "calculate-orientation-rectangles.pdf"). The following is an outline. <br>
![Notations](/images/161208-3d-reconstruction-notation.png "Notations") <br>
As shown in the picture above. $O$ is the optical center of the camera and $\vec z_1$ is its optical axis. $(O-xyz)$ is a 3D orthogonal coordinate system and $(O_0-uv)$ is the image plane with $OO$ as its image center. <br>

we are going to estimate the oriantation of the $plane(P_1-P_4)$, or more specifically: its normal vector $\vec V$, with its projection $PP_1-PP_4$ on the image plane.  <br>

The problem can be reduce to find the value of $z_2$ which can minimal the value of our object function: <br>
![object function](/images/161208-3d-reconstruction-objFunction.png "object function") <br>

where <br>
![variables](/images/161208-3d-reconstruction-vars.png "variables") <br>

$z_1$ = 3000 (or any other constant, all of which will lead to the same result of $\vec V$) <br>

Since our object function has only one variable, there are dozens of methods to find its minimal, I tried particle swarm optimization (PSO), and it worked well. <br>


Once we get the value of $z_2$, we get the value of $P_1-P_4$, with which, we can calculate the value of $\vec V$ easily. <br>

## 3D Scene Reconstruction(Orthographic projection)

Once we have the oriantations of all rectangles, we can infer their relative positions from the intersections in the photo and eventually reconstruct the whole scene. Although the low resoluction and some potential distortion in the photo may cause some error, they won’t have large impact to the whole model because the oriantations are calculated independently. <br>

# Experimental Results
I’m currently trying to verify my work on [NYU Depth Dataset V2](http://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) and compare with other works. Email me if you are interested about current results.
