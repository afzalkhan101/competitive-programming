<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 767A · Snacktower

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">data structures</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/767/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

According to an old legeng, a long time ago Ankh-Morpork residents did something wrong to miss Fortune, and she cursed them. She said that at some time n snacks of distinct sizes will fall on the city, and the residents should build a Snacktower of them by placing snacks one on another. Of course, big snacks should be at the bottom of the tower, while small snacks should be at the top.

Years passed, and once different snacks started to fall onto the city, and the residents began to build the Snacktower.

However, they faced some troubles. Each day exactly one snack fell onto the city, but their order was strange. So, at some days the residents weren't able to put the new stack on the top of the Snacktower: they had to wait until all the bigger snacks fell. Of course, in order to not to anger miss Fortune again, the residents placed each snack on the top of the tower immediately as they could do it.

Write a program that models the behavior of Ankh-Morpork residents.

## Input

The first line contains single integer n (1 ≤ n ≤ 100 000) — the total number of snacks.

The second line contains n integers, the i-th of them equals the size of the snack which fell on the i-th day. Sizes are distinct integers from 1 to n.

## Output

Print n lines. On the i-th of them print the sizes of the snacks which the residents placed on the top of the Snacktower on the i-th day in the order they will do that. If no snack is placed on some day, leave the corresponding line empty.

## Sample 1

Input

```text
3
3 1 2
```

Output

```text
3
2 1
```

## Sample 2

Input

```text
5
4 5 1 2 3
```

Output

```text
5 4
3 2 1
```

## Note

In the example a snack of size 3 fell on the first day, and the residents immediately placed it. On the second day a snack of size 1 fell, and the residents weren't able to place it because they were missing the snack of size 2. On the third day a snack of size 2 fell, and the residents immediately placed it. Right after that they placed the snack of size 1 which had fallen before.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
