---
layout: default
title: "[4.8]$\nabla$-SDF: Learning Euclidean Signed Distance Functions Online with Gradient-Augmented Octree Interpolation and Neural Residual"
---

# [4.8] $\nabla$-SDF: Learning Euclidean Signed Distance Functions Online with Gradient-Augmented Octree Interpolation and Neural Residual

- Authors: Zhirui Dai, Qihao Qian, Tianxing Fan, Nikolay Atanasov
- [arXiv Link](https://arxiv.org/abs/2510.18999v1)
- [PDF Link](https://arxiv.org/pdf/2510.18999v1.pdf)

## Subfields
 3D Reconstruction / Mapping (SDF)
## Reason for Interest

The paper introduces a mathematically grounded hybrid mapping approach (Gradient-Augmented Octree + Neural Residual) with solid theoretical proofs (error bounds). It demonstrates superior reconstruction accuracy and efficiency on indoor data compared to strong baselines like PIN-SLAM and Voxblox. However, the evaluation is entirely limited to small-scale indoor scenes (Replica). The lack of validation on large-scale outdoor autonomous driving datasets (e.g., KITTI, nuScenes) makes its direct effectiveness for 'car-side' applications unproven, heavily impacting the score under the strict AD-relevance criteria.
## Abstract: 

