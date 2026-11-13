# 1475A · Odd Divisor

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/1475/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You are given an integer $$$n$$$. Check if $$$n$$$ has an odd divisor, greater than one (does there exist such a number $$$x$$$ ($$$x > 1$$$) that $$$n$$$ is divisible by $$$x$$$ and $$$x$$$ is odd).

For example, if $$$n=6$$$, then there is $$$x=3$$$. If $$$n=4$$$, then such a number does not exist.

## Input

The first line contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. Then $$$t$$$ test cases follow.

Each test case contains one integer $$$n$$$ ($$$2 \le n \le 10^{14}$$$).

Please note, that the input for some test cases won't fit into $$$32$$$-bit integer type, so you should use at least $$$64$$$-bit integer type in your programming language.

## Output

For each test case, output on a separate line:

- "YES" if $$$n$$$ has an odd divisor, greater than one;
- "NO" otherwise.

You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).

## Sample 1

Input

```text
6
2
3
4
5
998244353
1099511627776
```

Output

```text
NO
YES
NO
YES
YES
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
