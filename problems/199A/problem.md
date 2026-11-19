<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 199A · Hexadecimal's theorem

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">brute force</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">implementation</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/199/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Recently, a chaotic virus Hexadecimal advanced a new theorem which will shake the Universe. She thinks that each Fibonacci number can be represented as sum of three not necessary different Fibonacci numbers.

Let's remember how Fibonacci numbers can be calculated. F0 = 0, F1 = 1, and all the next numbers are Fi = Fi - 2 + Fi - 1.

So, Fibonacci numbers make a sequence of numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...

If you haven't run away from the PC in fear, you have to help the virus. Your task is to divide given Fibonacci number n by three not necessary different Fibonacci numbers or say that it is impossible.

## Input

The input contains of a single integer n (0 ≤ n < 109) — the number that should be represented by the rules described above. It is guaranteed that n is a Fibonacci number.

## Output

Output three required numbers: a, b and c. If there is no answer for the test you have to print "I'm too stupid to solve this problem" without the quotes.

If there are multiple answers, print any of them.

## Sample 1

Input

```text
3
```

Output

```text
1 1 1
```

## Sample 2

Input

```text
13
```

Output

```text
2 3 8
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
