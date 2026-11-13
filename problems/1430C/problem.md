# 1430C · Numbers on Whiteboard

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">data structures</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/1430/C) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Numbers $$$1, 2, 3, \dots n$$$ (each integer from $$$1$$$ to $$$n$$$ once) are written on a board. In one operation you can erase any two numbers $$$a$$$ and $$$b$$$ from the board and write one integer $$$\frac{a + b}{2}$$$ rounded up instead.

You should perform the given operation $$$n - 1$$$ times and make the resulting number that will be left on the board as small as possible.

For example, if $$$n = 4$$$, the following course of action is optimal:

1. choose $$$a = 4$$$ and $$$b = 2$$$, so the new number is $$$3$$$, and the whiteboard contains $$$[1, 3, 3]$$$;
2. choose $$$a = 3$$$ and $$$b = 3$$$, so the new number is $$$3$$$, and the whiteboard contains $$$[1, 3]$$$;
3. choose $$$a = 1$$$ and $$$b = 3$$$, so the new number is $$$2$$$, and the whiteboard contains $$$[2]$$$.

It's easy to see that after $$$n - 1$$$ operations, there will be left only one number. Your goal is to minimize it.

## Input

The first line contains one integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.

The only line of each test case contains one integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the number of integers written on the board initially.

It's guaranteed that the total sum of $$$n$$$ over test cases doesn't exceed $$$2 \cdot 10^5$$$.

## Output

For each test case, in the first line, print the minimum possible number left on the board after $$$n - 1$$$ operations. Each of the next $$$n - 1$$$ lines should contain two integers — numbers $$$a$$$ and $$$b$$$ chosen and erased in each operation.

## Sample 1

Input

```text
1
4
```

Output

```text
2
2 4
3 3
3 1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
