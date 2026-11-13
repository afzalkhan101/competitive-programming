# 706A · Beru-taxi

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">geometry</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/706/A) · Rating 900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Vasiliy lives at point (a, b) of the coordinate plane. He is hurrying up to work so he wants to get out of his house as soon as possible. New app suggested n available Beru-taxi nearby. The i-th taxi is located at point (xi, yi) and moves with a speed vi.

Consider that each of n drivers will move directly to Vasiliy and with a maximum possible speed. Compute the minimum time when Vasiliy will get in any of Beru-taxi cars.

## Input

The first line of the input contains two integers a and b ( - 100 ≤ a, b ≤ 100) — coordinates of Vasiliy's home.

The second line contains a single integer n (1 ≤ n ≤ 1000) — the number of available Beru-taxi cars nearby.

The i-th of the following n lines contains three integers xi, yi and vi ( - 100 ≤ xi, yi ≤ 100, 1 ≤ vi ≤ 100) — the coordinates of the i-th car and its speed.

It's allowed that several cars are located at the same point. Also, cars may be located at exactly the same point where Vasiliy lives.

## Output

Print a single real value — the minimum time Vasiliy needs to get in any of the Beru-taxi cars. You answer will be considered correct if its absolute or relative error does not exceed 10 - 6.

Namely: let's assume that your answer is a, and the answer of the jury is b. The checker program will consider your answer correct, if $$\frac{|a-b|}{\max(1,b)} \leq 10^{-6}$$.

## Sample 1

Input

```text
0 0
2
2 0 1
0 2 2
```

Output

```text
1.00000000000000000000
```

## Sample 2

Input

```text
1 3
3
3 3 2
-2 3 6
-2 7 10
```

Output

```text
0.50000000000000000000
```

## Note

In the first sample, first taxi will get to Vasiliy in time 2, and second will do this in time 1, therefore 1 is the answer.

In the second sample, cars 2 and 3 will arrive simultaneously.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
