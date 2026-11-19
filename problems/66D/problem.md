<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 66D · Petya and His Friends

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/66/D) · Rating 1700

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Little Petya has a birthday soon. Due this wonderful event, Petya's friends decided to give him sweets. The total number of Petya's friends equals to n.

Let us remind you the definition of the greatest common divisor: GCD(a1, ..., ak) = d, where d represents such a maximal positive number that each ai (1 ≤ i ≤ k) is evenly divisible by d. At that, we assume that all ai's are greater than zero.

Knowing that Petya is keen on programming, his friends has agreed beforehand that the 1-st friend gives a1 sweets, the 2-nd one gives a2 sweets, ..., the n-th one gives an sweets. At the same time, for any i and j (1 ≤ i, j ≤ n) they want the GCD(ai, aj) not to be equal to 1. However, they also want the following condition to be satisfied: GCD(a1, a2, ..., an) = 1. One more: all the ai should be distinct.

Help the friends to choose the suitable numbers a1, ..., an.

## Input

The first line contains an integer n (2 ≤ n ≤ 50).

## Output

If there is no answer, print "-1" without quotes. Otherwise print a set of n distinct positive numbers a1, a2, ..., an. Each line must contain one number. Each number must consist of not more than 100 digits, and must not contain any leading zeros. If there are several solutions to that problem, print any of them.

Do not forget, please, that all of the following conditions must be true:

- For every i and j (1 ≤ i, j ≤ n): GCD(ai, aj) ≠ 1
- GCD(a1, a2, ..., an) = 1
- For every i and j (1 ≤ i, j ≤ n, i ≠ j): ai ≠ aj

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cout (also you may use %I64d).

## Sample 1

Input

```text
3
```

Output

```text
99
55
11115
```

## Sample 2

Input

```text
4
```

Output

```text
385
360
792
8360
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
