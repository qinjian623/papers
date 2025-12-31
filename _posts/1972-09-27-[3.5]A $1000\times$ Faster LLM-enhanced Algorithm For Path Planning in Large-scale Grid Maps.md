---
layout: default
title: "[3.5]A $1000\times$ Faster LLM-enhanced Algorithm For Path Planning in Large-scale Grid Maps"
---

# [3.5] A $1000\times$ Faster LLM-enhanced Algorithm For Path Planning in Large-scale Grid Maps

- Authors: Junlin Zeng, Xin Zhang, Xiang Zhao, Yan Pan
- [arXiv Link](https://arxiv.org/abs/2510.02716v2)
- [PDF Link](https://arxiv.org/pdf/2510.02716v2.pdf)

## Subfields
 Path Planning / Grid Map Search
## Reason for Interest

The paper presents an LLM-guided A* algorithm for grid maps. Its value for autonomous driving (AD) is limited (Score < 5) for several reasons: 1. **Lack of Kinematics**: The method plans on discrete grids without considering vehicle kinematics (non-holonomic constraints), making it unsuitable for real-world vehicle planning (e.g., parking) which requires continuous curvature (Hybrid A*). 2. **Weak Baselines**: The headline '1000x speedup' compares against a baseline with inefficient data structures (linear list lookup); the improvement over a standard optimized A* is much smaller (~11x). 3. **Computational Efficiency**: Using a 32B parameter LLM for pathfinding on small grids (450x450) introduces massive computational overhead compared to specialized geometric solvers (e.g., JPS) which are typically preferred in AD stacks. 4. **Synthetic Data**: Experiments use random grid maps rather than realistic driving scenarios or datasets.
## Abstract: 

