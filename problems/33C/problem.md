<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 33C · Wonderful Randomized Sum

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/33/C) · Rating 1800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Learn, learn and learn again — Valera has to do this every day. He is studying at mathematical school, where math is the main discipline. The mathematics teacher loves her discipline very much and tries to cultivate this love in children. That's why she always gives her students large and difficult homework. Despite that Valera is one of the best students, he failed to manage with the new homework. That's why he asks for your help. He has the following task. A sequence of n numbers is given. A prefix of a sequence is the part of the sequence (possibly empty), taken from the start of the sequence. A suffix of a sequence is the part of the sequence (possibly empty), taken from the end of the sequence. It is allowed to sequentially make two operations with the sequence. The first operation is to take some prefix of the sequence and multiply all numbers in this prefix by  - 1. The second operation is to take some suffix and multiply all numbers in it by  - 1. The chosen prefix and suffix may intersect. What is the maximum total sum of the sequence that can be obtained by applying the described operations?

## Input

The first line contains integer n (1 ≤ n ≤ 105) — amount of elements in the sequence. The second line contains n integers ai ( - 104 ≤ ai ≤ 104) — the sequence itself.

## Output

The first and the only line of the output should contain the answer to the problem.

## Sample 1

Input

```text
3
-1 -2 -3
```

Output

```text
6
```

## Sample 2

Input

```text
5
-4 2 0 5 0
```

Output

```text
11
```

## Sample 3

Input

```text
5
-1 10 -5 10 -2
```

Output

```text
18
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
