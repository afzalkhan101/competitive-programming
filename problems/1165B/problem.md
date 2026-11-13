# 1165B · Polycarp Training

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">data structures</span><span class="practice-tag">greedy</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/1165/B) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Polycarp wants to train before another programming competition. During the first day of his training he should solve exactly $$$1$$$ problem, during the second day — exactly $$$2$$$ problems, during the third day — exactly $$$3$$$ problems, and so on. During the $$$k$$$-th day he should solve $$$k$$$ problems.

Polycarp has a list of $$$n$$$ contests, the $$$i$$$-th contest consists of $$$a_i$$$ problems. During each day Polycarp has to choose exactly one of the contests he didn't solve yet and solve it. He solves exactly $$$k$$$ problems from this contest. Other problems are discarded from it. If there are no contests consisting of at least $$$k$$$ problems that Polycarp didn't solve yet during the $$$k$$$-th day, then Polycarp stops his training.

How many days Polycarp can train if he chooses the contests optimally?

## Input

The first line of the input contains one integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the number of contests.

The second line of the input contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 2 \cdot 10^5$$$) — the number of problems in the $$$i$$$-th contest.

## Output

Print one integer — the maximum number of days Polycarp can train if he chooses the contests optimally.

## Sample 1

Input

```text
4
3 1 4 1
```

Output

```text
3
```

## Sample 2

Input

```text
3
1 1 1
```

Output

```text
1
```

## Sample 3

Input

```text
5
1 1 1 2 2
```

Output

```text
2
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
