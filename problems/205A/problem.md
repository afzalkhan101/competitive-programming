# 205A · Little Elephant and Rozdil

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">brute force</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/205/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The Little Elephant loves Ukraine very much. Most of all he loves town Rozdol (ukr. "Rozdil").

However, Rozdil is dangerous to settle, so the Little Elephant wants to go to some other town. The Little Elephant doesn't like to spend much time on travelling, so for his journey he will choose a town that needs minimum time to travel to. If there are multiple such cities, then the Little Elephant won't go anywhere.

For each town except for Rozdil you know the time needed to travel to this town. Find the town the Little Elephant will go to or print "Still Rozdil", if he stays in Rozdil.

## Input

The first line contains a single integer n (1 ≤ n ≤ 105) — the number of cities. The next line contains n integers, separated by single spaces: the i-th integer represents the time needed to go from town Rozdil to the i-th town. The time values are positive integers, not exceeding 109.

You can consider the cities numbered from 1 to n, inclusive. Rozdil is not among the numbered cities.

## Output

Print the answer on a single line — the number of the town the Little Elephant will go to. If there are multiple cities with minimum travel time, print "Still Rozdil" (without the quotes).

## Sample 1

Input

```text
2
7 4
```

Output

```text
2
```

## Sample 2

Input

```text
7
7 4 47 100 4 9 12
```

Output

```text
Still Rozdil
```

## Note

In the first sample there are only two cities where the Little Elephant can go. The travel time for the first town equals 7, to the second one — 4. The town which is closest to Rodzil (the only one) is the second one, so the answer is 2.

In the second sample the closest cities are cities two and five, the travelling time to both of them equals 4, so the answer is "Still Rozdil".

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
