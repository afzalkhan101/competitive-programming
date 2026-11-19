<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 194A · Exams

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/194/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

One day the Codeforces round author sat exams. He had n exams and he needed to get an integer from 2 to 5 for each exam. He will have to re-sit each failed exam, i.e. the exam that gets mark 2.

The author would need to spend too much time and effort to make the sum of his marks strictly more than k. That could have spoilt the Codeforces round. On the other hand, if the sum of his marks is strictly less than k, the author's mum won't be pleased at all.

The Codeforces authors are very smart and they always get the mark they choose themselves. Also, the Codeforces authors just hate re-sitting exams.

Help the author and find the minimum number of exams he will have to re-sit if he passes the exams in the way that makes the sum of marks for all n exams equal exactly k.

## Input

The single input line contains space-separated integers n and k (1 ≤ n ≤ 50, 1 ≤ k ≤ 250) — the number of exams and the required sum of marks.

It is guaranteed that there exists a way to pass n exams in the way that makes the sum of marks equal exactly k.

## Output

Print the single number — the minimum number of exams that the author will get a 2 for, considering that the sum of marks for all exams must equal k.

## Sample 1

Input

```text
4 8
```

Output

```text
4
```

## Sample 2

Input

```text
4 10
```

Output

```text
2
```

## Sample 3

Input

```text
1 3
```

Output

```text
0
```

## Note

In the first sample the author has to get a 2 for all his exams.

In the second sample he should get a 3 for two exams and a 2 for two more.

In the third sample he should get a 3 for one exam.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
