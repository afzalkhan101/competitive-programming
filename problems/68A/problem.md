<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 68A · Irrational problem

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/68/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Little Petya was given this problem for homework:

You are given function $$f(x) = (((x \mod p_{1}) \mod p_{2}) \mod p_{3}) \mod p_{4}$$ (here $$\bmod$$ represents the operation of taking the remainder). His task is to count the number of integers x in range [a;b] with property f(x) = x.

It is a pity that Petya forgot the order in which the remainders should be taken and wrote down only 4 numbers. Each of 24 possible orders of taking the remainder has equal probability of being chosen. For example, if Petya has numbers 1, 2, 3, 4 then he can take remainders in that order or first take remainder modulo 4, then modulo 2, 3, 1. There also are 22 other permutations of these numbers that represent orders in which remainder can be taken. In this problem 4 numbers wrote down by Petya will be pairwise distinct.

Now it is impossible for Petya to complete the task given by teacher but just for fun he decided to find the number of integers $$x \in [a;b]$$ with property that probability that f(x) = x is not less than 31.4159265352718281828459045%. In other words, Petya will pick up the number x if there exist at least 7 permutations of numbers p1, p2, p3, p4, for which f(x) = x.

## Input

First line of the input will contain 6 integers, separated by spaces: p1, p2, p3, p4, a, b (1 ≤ p1, p2, p3, p4 ≤ 1000, 0 ≤ a ≤ b ≤ 31415).

It is guaranteed that numbers p1, p2, p3, p4 will be pairwise distinct.

## Output

Output the number of integers in the given range that have the given property.

## Sample 1

Input

```text
2 7 1 8 2 8
```

Output

```text
0
```

## Sample 2

Input

```text
20 30 40 50 0 100
```

Output

```text
20
```

## Sample 3

Input

```text
31 41 59 26 17 43
```

Output

```text
9
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
