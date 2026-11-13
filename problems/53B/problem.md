# 53B · Blog Photo

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">binary search</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/53/B) · Rating 1700

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

One popular blog site edits the uploaded photos like this. It cuts a rectangular area out of them so that the ratio of height to width (i.e. the height / width quotient) can vary from 0.8 to 1.25 inclusively. Besides, at least one side of the cut area should have a size, equal to some power of number 2 (2x for some integer x). If those rules don't indicate the size of the cut are clearly, then the way with which the cut part possesses the largest area is chosen. Of course, both sides of the cut area should be integer. If there are several answers to this problem, you should choose the answer with the maximal height.

## Input

The first line contains a pair of integers h and w (1 ≤ h, w ≤ 109) which are the height and width of the uploaded photo in pixels.

## Output

Print two integers which are the height and width of the cut area.

## Sample 1

Input

```text
2 1
```

Output

```text
1 1
```

## Sample 2

Input

```text
2 2
```

Output

```text
2 2
```

## Sample 3

Input

```text
5 5
```

Output

```text
5 4
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
