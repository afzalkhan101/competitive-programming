# 60C · Mushroom Strife

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/60/C) · Rating 2100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Pasha and Akim were making a forest map — the lawns were the graph's vertexes and the roads joining the lawns were its edges. They decided to encode the number of laughy mushrooms on every lawn in the following way: on every edge between two lawns they wrote two numbers, the greatest common divisor (GCD) and the least common multiple (LCM) of the number of mushrooms on these lawns. But one day Pasha and Akim had an argument about the laughy mushrooms and tore the map. Pasha was left with just some part of it, containing only m roads. Your task is to help Pasha — use the map he has to restore the number of mushrooms on every lawn. As the result is not necessarily unique, help Pasha to restore any one or report that such arrangement of mushrooms does not exist. It is guaranteed that the numbers on the roads on the initial map were no less that 1 and did not exceed 106.

## Input

The first line contains two numbers n and m ($$1 \leq n \leq 100, 0 \leq m \leq \frac{n(n-1)}{2}$$) which are the numbers of lawns and roads we know about. Each of the following m lines contains four numbers which are the numbers of lawns the road connects, the GCD and the LCM of the numbers of mushrooms on these lawns (1 ≤ GCD, LCM ≤ 106).

It is guaranteed, that no road connects lawn to itself, and no two lawns are connected by more than one road.

## Output

The answer should contain "YES" or "NO" on the first line, saying whether it is possible or not to perform the arrangement. If the answer is "YES", print on the following line n numbers which are the numbers of mushrooms on the corresponding lawns.

## Sample 1

Input

```text
1 0
```

Output

```text
YES
1
```

## Sample 2

Input

```text
2 1
1 2 1 3
```

Output

```text
YES
1 3
```

## Sample 3

Input

```text
3 2
3 2 1 2
3 1 1 10
```

Output

```text
YES
5 1 2
```

## Sample 4

Input

```text
2 1
1 2 3 7
```

Output

```text
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
