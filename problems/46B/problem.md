<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 46B · T-shirts from Sponsor

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/46/B) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

One day a well-known sponsor of a well-known contest decided to give every participant of the contest a T-shirt as a present. A natural problem occurred: on the one hand, it is not clear how many T-shirts of what sizes should be ordered, and on the other hand, one doesn't want to order too many T-shirts (and we do not exactly paper the walls with the oversupply). After considerable brain racking and some pre-estimating, the sponsor representatives ordered a certain number of T-shirts of sizes S, M, L, XL and XXL. The T-shirts turned out to bring good luck, that's why on the contest day there built up a line of K participants willing to get one. Every contestant is characterized by his/her desired T-shirt size (so it happens that for all the participants it is also one of the sizes S, M, L, XL and XXL). The participants come up to get a T-shirt one by one and try to choose the most suitable one, choosing it like this. If there is still a T-shirt of the optimal size left, that he/she takes it without further ado. Otherwise the contestant would prefer to choose a T-shirt with the size as close to the optimal one as possible (the distance between neighboring sizes is considered equal to one). If the variant of choice is not unique, the contestant will take a T-shirt of a bigger size (in case he/she grows more). For example, for a person whose optimal size is L the preference list looks like this: L, XL, M, XXL, S. Using the data on how many T-shirts of every size had been ordered by the organizers, on the size of contestants in the line determine who got a T-shirt of what size.

## Input

The first line contains five non-negative integers NS, NM, NL, NXL, NXXL not exceeding 1000 which represent the number of T-shirts of the corresponding sizes. The second line contains an integer K (1 ≤ K ≤ 1000) which represents the number of participants. The next K lines contain the optimal T-shirt sizes for the contestants. The sizes are given in the order in which the participants stand in the line. It is guaranteed that NS + NM + NL + NXL + NXXL ≥ K.

## Output

For each contestant, print a line containing the size of the T-shirt he/she got.

## Sample 1

Input

```text
1 0 2 0 1
3
XL
XXL
M
```

Output

```text
XXL
L
L
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
