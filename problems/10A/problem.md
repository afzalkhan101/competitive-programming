# 10A · Power Consumption Calculation

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/10/A) · Rating 900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P1 watt per minute. T1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P2 watt per minute. Finally, after T2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P3 watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into n time periods [l1, r1], [l2, r2], ..., [ln, rn]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l1, rn].

## Input

The first line contains 6 integer numbers n, P1, P2, P3, T1, T2 (1 ≤ n ≤ 100, 0 ≤ P1, P2, P3 ≤ 100, 1 ≤ T1, T2 ≤ 60). The following n lines contain description of Tom's work. Each i-th of these lines contains two space-separated integers li and ri (0 ≤ li < ri ≤ 1440, ri < li + 1 for i < n), which stand for the start and the end of the i-th period of work.

## Output

Output the answer to the problem.

## Sample 1

Input

```text
1 3 2 1 5 10
0 10
```

Output

```text
30
```

## Sample 2

Input

```text
2 8 4 2 5 10
20 30
50 100
```

Output

```text
570
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
