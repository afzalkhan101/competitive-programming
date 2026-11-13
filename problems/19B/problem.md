# 19B · Checkout Assistant

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">dp</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/19/B) · Rating 1900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Bob came to a cash & carry store, put n items into his trolley, and went to the checkout counter to pay. Each item is described by its price ci and time ti in seconds that a checkout assistant spends on this item. While the checkout assistant is occupied with some item, Bob can steal some other items from his trolley. To steal one item Bob needs exactly 1 second. What is the minimum amount of money that Bob will have to pay to the checkout assistant? Remember, please, that it is Bob, who determines the order of items for the checkout assistant.

## Input

The first input line contains number n (1 ≤ n ≤ 2000). In each of the following n lines each item is described by a pair of numbers ti, ci (0 ≤ ti ≤ 2000, 1 ≤ ci ≤ 109). If ti is 0, Bob won't be able to steal anything, while the checkout assistant is occupied with item i.

## Output

Output one number — answer to the problem: what is the minimum amount of money that Bob will have to pay.

## Sample 1

Input

```text
4
2 10
0 20
1 5
1 3
```

Output

```text
8
```

## Sample 2

Input

```text
3
0 1
0 10
0 100
```

Output

```text
111
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
