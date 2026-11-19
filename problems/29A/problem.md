<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 29A · Spit Problem

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">brute force</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/29/A) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

In a Berland's zoo there is an enclosure with camels. It is known that camels like to spit. Bob watched these interesting animals for the whole day and registered in his notepad where each animal spitted. Now he wants to know if in the zoo there are two camels, which spitted at each other. Help him to solve this task.

The trajectory of a camel's spit is an arc, i.e. if the camel in position x spits d meters right, he can hit only the camel in position x + d, if such a camel exists.

## Input

The first line contains integer n (1 ≤ n ≤ 100) — the amount of camels in the zoo. Each of the following n lines contains two integers xi and di ( - 104 ≤ xi ≤ 104, 1 ≤ |di| ≤ 2·104) — records in Bob's notepad. xi is a position of the i-th camel, and di is a distance at which the i-th camel spitted. Positive values of di correspond to the spits right, negative values correspond to the spits left. No two camels may stand in the same position.

## Output

If there are two camels, which spitted at each other, output YES. Otherwise, output NO.

## Sample 1

Input

```text
2
0 1
1 -1
```

Output

```text
YES
```

## Sample 2

Input

```text
3
0 1
1 1
2 -2
```

Output

```text
NO
```

## Sample 3

Input

```text
5
2 -10
3 10
0 5
5 -5
10 1
```

Output

```text
YES
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
