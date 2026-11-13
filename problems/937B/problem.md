# 937B · Vile Grasshoppers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/937/B) · Rating 1400

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

The weather is fine today and hence it's high time to climb the nearby pine and enjoy the landscape.

The pine's trunk includes several branches, located one above another and numbered from 2 to y. Some of them (more precise, from 2 to p) are occupied by tiny vile grasshoppers which you're at war with. These grasshoppers are known for their awesome jumping skills: the grasshopper at branch x can jump to branches $$2 \cdot x, 3 \cdot x, \ldots, \left\lfloor \frac{y}{x} \right\rfloor \cdot x$$.

Keeping this in mind, you wisely decided to choose such a branch that none of the grasshoppers could interrupt you. At the same time you wanna settle as high as possible since the view from up there is simply breathtaking.

In other words, your goal is to find the highest branch that cannot be reached by any of the grasshoppers or report that it's impossible.

## Input

The only line contains two integers p and y (2 ≤ p ≤ y ≤ 109).

## Output

Output the number of the highest suitable branch. If there are none, print -1 instead.

## Sample 1

Input

```text
3 6
```

Output

```text
5
```

## Sample 2

Input

```text
3 4
```

Output

```text
-1
```

## Note

In the first sample case grasshopper from branch 2 reaches branches 2, 4 and 6 while branch 3 is initially settled by another grasshopper. Therefore the answer is 5.

It immediately follows that there are no valid branches in second sample case.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
