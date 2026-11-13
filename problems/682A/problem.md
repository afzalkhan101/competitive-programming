# 682A · Alyona and Numbers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/682/A) · Rating 1100

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

After finishing eating her bun, Alyona came up with two integers n and m. She decided to write down two columns of integers — the first column containing integers from 1 to n and the second containing integers from 1 to m. Now the girl wants to count how many pairs of integers she can choose, one from the first column and the other from the second column, such that their sum is divisible by 5.

Formally, Alyona wants to count the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and $$(x+y) \mod 5$$ equals 0.

As usual, Alyona has some troubles and asks you to help.

## Input

The only line of the input contains two integers n and m (1 ≤ n, m ≤ 1 000 000).

## Output

Print the only integer — the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and (x + y) is divisible by 5.

## Sample 1

Input

```text
6 12
```

Output

```text
14
```

## Sample 2

Input

```text
11 14
```

Output

```text
31
```

## Sample 3

Input

```text
1 5
```

Output

```text
1
```

## Sample 4

Input

```text
3 8
```

Output

```text
5
```

## Sample 5

Input

```text
5 7
```

Output

```text
7
```

## Sample 6

Input

```text
21 21
```

Output

```text
88
```

## Note

Following pairs are suitable in the first sample case:

- for x = 1 fits y equal to 4 or 9;
- for x = 2 fits y equal to 3 or 8;
- for x = 3 fits y equal to 2, 7 or 12;
- for x = 4 fits y equal to 1, 6 or 11;
- for x = 5 fits y equal to 5 or 10;
- for x = 6 fits y equal to 4 or 9.

Only the pair (1, 4) is suitable in the third sample case.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
