---
layout: post
title: Some research summary
---

The goal for my research is to build a system that reconstruct and update moving bodies with moving cameras on AR glasses. 
This task is difficult because both the target body shape and the viewpoint are changing all the time. 
And it is also difficult to find good feature points on the cloth texture to align results from different view and in different time.  
So, we start by building our own capture system.

## 3D poses collection:

Our capture system consists of 5 synchronized cameras: 3 world view cameras fixed on tripods and 2 moving cameras fixed on a 3D printed AR glasses (one for body capture and one for SLAM localization). 
With this system, we can get the 3d poses of both body joints and the moving cameras.
![cameras](/images/201112-1-all_cameras.png "cameras") <br>
![glasses](/images/201112-2-glasses_loc.jpg "glasses localization") <br>

## SMPL model fitting and texture generating
The body shape is too complicated to generate directly from RGB images, so we chose the [SMPL](https://smpl.is.tue.mpg.de/) model. 
[Smplify-X](https://smpl-x.is.tue.mpg.de/) and [VIBE](https://github.com/mkocabas/VIBE) are good methods to fit SMPL model to RGB images, but the result is not good enough for texture generating. 
So, we use a boundary loss to refine the body fitting and the as-rigid-as-possible method to refine the face mesh. 
The result improved a bit, but it is still not good enough and it is also difficult to integrate the textures form different views in different time points. 

![cameras](/images/201112-3-boundary_loss.png "boundary_loss") <br>
![glasses](/images/201112-4-texture_pipeline.png "texture_pipeline") <br>

## TSDF based methods:
Beside predefined model-based reconstruction, there are some other methods like [KinectFusion](https://www.microsoft.com/en-us/research/publication/kinectfusion-real-time-3d-reconstruction-and-interaction-using-a-moving-depth-camera/), 
[Fusion4D](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/a114-dou.pdf) and [DynamicFusion](https://grail.cs.washington.edu/projects/dynamicfusion/) that based on the TSDF volume. 
This is a powerful method that good at reconstructing and update shape and texture for arbitrary 3d object.  
I am still working on this and I have a feeling that this is a right way for 3d body pre-scan.
![glasses](/images/201112-5-Qian_TSDF.png "TSDF mesh") <br>
RGBD images scanned with [Realsense D435](https://www.intelrealsense.com/zh-hans/depth-camera-d435/) and data processed with [Open3d](http://www.open3d.org/).

I'm seeking a 2021 summer internship position in AR/VR, 3D reconstruction or SLAM. Please let me know if you are interested in my research. My email is qzane[at]cs.unc.com
