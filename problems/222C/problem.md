<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 222C · Reducing Fractions

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/222/C) · Rating 1800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

To confuse the opponents, the Galactic Empire represents fractions in an unusual format. The fractions are represented as two sets of integers. The product of numbers from the first set gives the fraction numerator, the product of numbers from the second set gives the fraction denominator. However, it turned out that the programs that work with fractions in this representations aren't complete, they lack supporting the operation of reducing fractions. Implement this operation and the Empire won't forget you.

## Input

The first input line contains two space-separated integers n, m (1 ≤ n, m ≤ 105) that show how many numbers the first set (the numerator) and the second set (the denominator) contain, correspondingly.

The second line contains n space-separated integers: a1, a2, ..., an (1 ≤ ai ≤ 107) — the numbers that are multiplied to produce the numerator.

The third line contains m space-separated integers: b1, b2, ..., bm (1 ≤ bi ≤ 107) — the numbers that are multiplied to produce the denominator.

## Output

Print the answer to the problem in the form, similar to the form of the input data. The number of values in the sets you print nout, mout must satisfy the inequality 1 ≤ nout, mout ≤ 105, and the actual values in the sets aout, i and bout, i must satisfy the inequality 1 ≤ aout, i, bout, i ≤ 107.

Separate the values in the lines by spaces. The printed fraction must be reduced, that is, there mustn't be such integer x (x > 1), that the numerator and the denominator of the printed fraction are divisible by x. If there are several matching answers, print any of them.

## Sample 1

Input

```text
3 2
100 5 2
50 10
```

Output

```text
2 3
2 1
1 1 1
```

## Sample 2

Input

```text
4 3
2 5 10 20
100 1 3
```

Output

```text
1 1
20
3
```

## Note

In the first test sample the numerator equals 1000, the denominator equals 500. If we reduce fraction 1000/500 by the greatest common divisor of the numerator and the denominator (by 500), we obtain fraction 2/1.

In the second test sample the numerator equals 2000, the denominator equals 300. If we reduce fraction 2000/300 by the greatest common divisor of the numerator and the denominator (by 100), we obtain fraction 20/3.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
