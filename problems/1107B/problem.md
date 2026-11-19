<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 1107B · Digital root

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/1107/B) · Rating 1000

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Today at the lesson of mathematics, Petya learns about the digital root.

The digital root of a non-negative integer is the single digit value obtained by an iterative process of summing digits, on each iteration using the result from the previous iteration to compute a digit sum. The process continues until a single-digit number is reached.

Let's denote the digital root of $$$x$$$ as $$$S(x)$$$. Then $$$S(5)=5$$$, $$$S(38)=S(3+8=11)=S(1+1=2)=2$$$, $$$S(10)=S(1+0=1)=1$$$.

As a homework Petya got $$$n$$$ tasks of the form: find $$$k$$$-th positive number whose digital root is $$$x$$$.

Petya has already solved all the problems, but he doesn't know if it's right. Your task is to solve all $$$n$$$ tasks from Petya's homework.

## Input

The first line contains a single integer $$$n$$$ ($$$1 \le n \le 10^3$$$) — the number of tasks in Petya's homework. The next $$$n$$$ lines contain two integers $$$k_i$$$ ($$$1 \le k_i \le 10^{12}$$$) and $$$x_i$$$ ($$$1 \le x_i \le 9$$$) — $$$i$$$-th Petya's task in which you need to find a $$$k_i$$$-th positive number, the digital root of which is $$$x_i$$$.

## Output

Output $$$n$$$ lines, $$$i$$$-th line should contain a single integer — the answer to the $$$i$$$-th problem.

## Sample 1

Input

```text
3
1 5
5 2
3 1
```

Output

```text
5
38
19
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
