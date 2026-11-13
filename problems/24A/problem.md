# 24A · Ring road

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/24/A) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Nowadays the one-way traffic is introduced all over the world in order to improve driving safety and reduce traffic jams. The government of Berland decided to keep up with new trends. Formerly all n cities of Berland were connected by n two-way roads in the ring, i. e. each city was connected directly to exactly two other cities, and from each city it was possible to get to any other city. Government of Berland introduced one-way traffic on all n roads, but it soon became clear that it's impossible to get from some of the cities to some others. Now for each road is known in which direction the traffic is directed at it, and the cost of redirecting the traffic. What is the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other?

## Input

The first line contains integer n (3 ≤ n ≤ 100) — amount of cities (and roads) in Berland. Next n lines contain description of roads. Each road is described by three integers ai, bi, ci (1 ≤ ai, bi ≤ n, ai ≠ bi, 1 ≤ ci ≤ 100) — road is directed from city ai to city bi, redirecting the traffic costs ci.

## Output

Output single integer — the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other.

## Sample 1

Input

```text
3
1 3 1
1 2 1
3 2 1
```

Output

```text
1
```

## Sample 2

Input

```text
3
1 3 1
1 2 5
3 2 1
```

Output

```text
2
```

## Sample 3

Input

```text
6
1 5 4
5 3 8
2 4 15
1 6 16
2 3 23
4 6 42
```

Output

```text
39
```

## Sample 4

Input

```text
4
1 2 9
2 3 8
3 4 7
4 1 5
```

Output

```text
0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
