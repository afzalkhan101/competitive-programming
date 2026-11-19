<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 32A · Reconnaissance

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">brute force</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/32/A) · Rating 800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

According to the regulations of Berland's army, a reconnaissance unit should consist of exactly two soldiers. Since these two soldiers shouldn't differ much, their heights can differ by at most d centimeters. Captain Bob has n soldiers in his detachment. Their heights are a1, a2, ..., an centimeters. Some soldiers are of the same height. Bob wants to know, how many ways exist to form a reconnaissance unit of two soldiers from his detachment.

Ways (1, 2) and (2, 1) should be regarded as different.

## Input

The first line contains two integers n and d (1 ≤ n ≤ 1000, 1 ≤ d ≤ 109) — amount of soldiers in Bob's detachment and the maximum allowed height difference respectively. The second line contains n space-separated integers — heights of all the soldiers in Bob's detachment. These numbers don't exceed 109.

## Output

Output one number — amount of ways to form a reconnaissance unit of two soldiers, whose height difference doesn't exceed d.

## Sample 1

Input

```text
5 10
10 20 50 60 65
```

Output

```text
6
```

## Sample 2

Input

```text
5 1
55 30 29 31 55
```

Output

```text
6
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
