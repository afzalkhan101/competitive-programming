<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 91B · Queue

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">binary search</span><span class="practice-tag">data structures</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/91/B) · Rating 1500

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

There are n walruses standing in a queue in an airport. They are numbered starting from the queue's tail: the 1-st walrus stands at the end of the queue and the n-th walrus stands at the beginning of the queue. The i-th walrus has the age equal to ai.

The i-th walrus becomes displeased if there's a younger walrus standing in front of him, that is, if exists such j (i < j), that ai > aj. The displeasure of the i-th walrus is equal to the number of walruses between him and the furthest walrus ahead of him, which is younger than the i-th one. That is, the further that young walrus stands from him, the stronger the displeasure is.

The airport manager asked you to count for each of n walruses in the queue his displeasure.

## Input

The first line contains an integer n (2 ≤ n ≤ 105) — the number of walruses in the queue. The second line contains integers ai (1 ≤ ai ≤ 109).

Note that some walruses can have the same age but for the displeasure to emerge the walrus that is closer to the head of the queue needs to be strictly younger than the other one.

## Output

Print n numbers: if the i-th walrus is pleased with everything, print "-1" (without the quotes). Otherwise, print the i-th walrus's displeasure: the number of other walruses that stand between him and the furthest from him younger walrus.

## Sample 1

Input

```text
6
10 8 5 3 50 45
```

Output

```text
2 1 0 -1 0 -1
```

## Sample 2

Input

```text
7
10 4 6 3 2 8 15
```

Output

```text
4 2 1 0 -1 -1 -1
```

## Sample 3

Input

```text
5
10 3 1 10 11
```

Output

```text
1 0 -1 -1 -1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
