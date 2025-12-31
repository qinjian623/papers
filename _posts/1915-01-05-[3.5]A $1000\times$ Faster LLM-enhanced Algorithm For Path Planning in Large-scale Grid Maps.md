---
layout: default
title: "[3.5]A $1000\times$ Faster LLM-enhanced Algorithm For Path Planning in Large-scale Grid Maps"
---

# [3.5] A $1000\times$ Faster LLM-enhanced Algorithm For Path Planning in Large-scale Grid Maps

- Authors: Junlin Zeng, Xin Zhang, Xiang Zhao, Yan Pan
- [arXiv Link](https://arxiv.org/abs/2510.02716)
- [PDF Link](https://arxiv.org/pdf/2510.02716.pdf)

## Subfields
 规划控制 / 路径规划
## Reason for Interest

该论文虽然探讨了LLM在路径规划中的应用，但对自动驾驶领域的实际价值较低，评分理由如下：
1. 场景建模过于简化：论文使用无运动学约束（Holonomic）的2D栅格地图进行A*搜索，未考虑车辆非完整约束（如转弯半径），无法直接应用于自动驾驶泊车或行车规划（通常需Hybrid A*或Lattice规划）。
2. 创新性不足与基线缺陷：论文将“使用哈希表优化A*的Closed List”列为核心创新点之一，这属于计算机基础数据结构优化，而非科研创新。这同时揭示了其对比基线（LLM-A*）存在实现极其低效的问题（线性查找），导致“1000倍加速”的结论具有误导性。
3. 实际收益有限：在与正常优化的A*（Opt-A*）对比中，仅在极大规模地图（450x450）下体现出LLM启发式的优势（约11倍加速），但在中小规模地图中优势不明显甚至更慢。
4. 缺乏实车相关性：属于通用机器人/算法研究，缺乏针对车端感控系统的适配。
## Abstract: 
Path planning in grid maps, arising from various applications, has garnered significant attention. Existing methods, such as A*, Dijkstra, and their variants, work well for small-scale maps but fail to address large-scale ones due to high search time and memory consumption. Recently, Large Language Models (LLMs) have shown remarkable performance in path planning but still suffer from spatial illusion and poor planning performance. Among all the works, LLM-A* \cite{meng2024llm} leverages LLM to generate a series of waypoints and then uses A* to plan the paths between the neighboring waypoints. In this way, the complete path is constructed. However, LLM-A* still suffers from high computational time for large-scale maps. To fill this gap, we conducted a deep investigation into LLM-A* and found its bottleneck, resulting in limited performance. Accordingly, we design an innovative LLM-enhanced algorithm, abbr. as iLLM-A*. iLLM-A* includes 3 carefully designed mechanisms, including the optimization of A*, an incremental learning method for LLM to generate high-quality waypoints, and the selection of the appropriate waypoints for A* for path planning. Finally, a comprehensive evaluation on various grid maps shows that, compared with LLM-A*, iLLM-A* \textbf{1) achieves more than $1000\times$ speedup on average, and up to $2349.5\times$ speedup in the extreme case, 2) saves up to $58.6\%$ of the memory cost, 3) achieves both obviously shorter path length and lower path length standard deviation.}
