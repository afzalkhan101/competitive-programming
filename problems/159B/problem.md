# 159B · Matchmaker

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">*special</span><span class="practice-tag">greedy</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/159/B) · Rating 1100

Time: 3.0 seconds · Memory: 256.0 MB

## Problem

Polycarpus has n markers and m marker caps. Each marker is described by two numbers: xi is the color and yi is the diameter. Correspondingly, each cap is described by two numbers: aj is the color and bj is the diameter. Cap (aj, bj) can close marker (xi, yi) only if their diameters match, that is, bj = yi. Besides, a marker is considered to be beautifully closed, if the cap color and the marker color match, that is, aj = xi.

Find the way to close the maximum number of markers. If there are several such ways, then choose the one that has the maximum number of beautifully closed markers.

## Input

The first input line contains two space-separated integers n and m (1 ≤ n, m ≤ 105) — the number of markers and the number of caps, correspondingly.

Next n lines describe the markers. The i-th line contains two space-separated integers xi, yi (1 ≤ xi, yi ≤ 1000) — the i-th marker's color and diameter, correspondingly.

Next m lines describe the caps. The j-th line contains two space-separated integers aj, bj (1 ≤ aj, bj ≤ 1000) — the color and diameter of the j-th cap, correspondingly.

## Output

Print two space-separated integers u, v, where u is the number of closed markers and v is the number of beautifully closed markers in the sought optimal way. Remember that you have to find the way to close the maximum number of markers, and if there are several such ways, you should choose the one where the number of beautifully closed markers is maximum.

## Sample 1

Input

```text
3 4
1 2
3 4
2 4
5 4
2 4
1 1
1 2
```

Output

```text
3 2
```

## Sample 2

Input

```text
2 2
1 2
2 1
3 4
5 1
```

Output

```text
1 0
```

## Note

In the first test sample the first marker should be closed by the fourth cap, the second marker should be closed by the first cap and the third marker should be closed by the second cap. Thus, three markers will be closed, and two of them will be beautifully closed — the first and the third markers.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
