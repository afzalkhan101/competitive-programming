# 34A · Reconnaissance 2

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/34/A) · Rating 800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

n soldiers stand in a circle. For each soldier his height ai is known. A reconnaissance unit can be made of such two neighbouring soldiers, whose heights difference is minimal, i.e. |ai - aj| is minimal. So each of them will be less noticeable with the other. Output any pair of soldiers that can form a reconnaissance unit.

## Input

The first line contains integer n (2 ≤ n ≤ 100) — amount of soldiers. Then follow the heights of the soldiers in their order in the circle — n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 1000). The soldier heights are given in clockwise or counterclockwise direction.

## Output

Output two integers — indexes of neighbouring soldiers, who should form a reconnaissance unit. If there are many optimum solutions, output any of them. Remember, that the soldiers stand in a circle.

## Sample 1

Input

```text
5
10 12 13 15 10
```

Output

```text
5 1
```

## Sample 2

Input

```text
4
10 20 30 40
```

Output

```text
1 2
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
