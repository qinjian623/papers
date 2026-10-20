# Monte-Carlo TopK: Fast Top-K Selection for Vector Search Scores

**Jian Qin · June 2026 · Preprint manuscript · 10 pages**

[PDF](paper.pdf) · [LaTeX source](source/) · [FAISS implementation](https://github.com/qinjian623/faiss/tree/e2ef9c7de793d208652979f1d03cc0545fdd482d)

## Abstract

Flat vector search computes one score per database vector and then selects the best K scores. On modern GPU baselines, this final selection can be a large part of the search time. Monte-Carlo TopK reduces this cost with a simple post-score selector. For each query, it samples a small set of scores, chooses a sampled threshold, filters the full score row once, and runs exact top-K only on the surviving candidates. In exact mode, rows with too few or too many candidates fall back to exact selection; an optional capped mode trades exact agreement for bounded work. In FAISS GPU flat-search tests on four ANN10M squared-L2 benchmarks, Monte-Carlo TopK gives a 15.0x selector speedup and a 2.62–2.83x end-to-end speedup, with zero fallbacks across five sample seeds. On SIFT1M, a no-fallback setting gives a 10.0x selector speedup and a 2.72x end-to-end speedup.

## Build

Requires pdfLaTeX, BibTeX, latexmk, and TeX Live packages for AMS, graphics, booktabs, float, geometry, fancyhdr, placeins, microtype, natbib, hyperref, and Times fonts. The local `arxiv.sty` is included.

```sh
cd papers/mc-topk/source
make pdf
# Produces main.pdf

make arxiv
# Produces arxiv-monte-carlo-topk.tar.gz
```

Builds do not replace the displayed `paper.pdf`. When publishing a revision, review the new PDF, replace it, and update the version information and `SHA256SUMS`.

## Version

- Original manuscript: `qinjian623/pytorch_vec_search`, branch `migration/mac-20260913`, commit `be03e8a9a737cd6adb2adeac2dfc4e513a5b5e8d` (July 17, 2026, 15:23:05 UTC).
- `source/` contains 21 unchanged build inputs from that commit, including seven PDF figures, eight section files, the bibliography, style, and Makefile.
- `paper.pdf` is the 10-page build produced on October 9, 2026. The manuscript has not been revised for this collection.
- Related implementation: [FAISS commit e2ef9c7de793](https://github.com/qinjian623/faiss/commit/e2ef9c7de793d208652979f1d03cc0545fdd482d). The selector is in `faiss/gpu/utils/MonteCarloTopK.cu` and `.cuh`; tests and some benchmark drivers are in `faiss/gpu/test/`.
- `SHA256SUMS` records the SHA-256 hashes of the displayed PDF and the 21 source files.

## Experimental materials and limitations

This directory includes the buildable manuscript and its figures. Host scripts, command records, datasets, and experiment result directories from the original project are not included. The reported experiments have not been rerun for this collection.

The complete drivers for all reported ANN10M GPU xbin and CPU experiments were not found in the available commits. The public FAISS code therefore does not establish that every experiment can be rerun. The manuscript's Code Availability section is preserved as written and should be read with this limitation. Inner-product search, cosine search, and other hardware require separate evaluation.

## Citation and use

Jian Qin. *Monte-Carlo TopK: Fast Top-K Selection for Vector Search Scores*. June 2026. Preprint manuscript; source revision July 17, 2026.

No arXiv identifier, DOI, or venue is listed; no publication or acceptance is claimed. Rights to the manuscript and figures are reserved by the author. The FAISS code is covered by its repository's MIT license.
