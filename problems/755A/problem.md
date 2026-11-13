# 755A · PolandBall and Hypothesis

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">graphs</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/755/A) · Rating 800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

PolandBall is a young, clever Ball. He is interested in prime numbers. He has stated a following hypothesis: "There exists such a positive integer n that for each positive integer m number n·m + 1 is a prime number".

Unfortunately, PolandBall is not experienced yet and doesn't know that his hypothesis is incorrect. Could you prove it wrong? Write a program that finds a counterexample for any n.

## Input

The only number in the input is n (1 ≤ n ≤ 1000) — number from the PolandBall's hypothesis.

## Output

Output such m that n·m + 1 is not a prime number. Your answer will be considered correct if you output any suitable m such that 1 ≤ m ≤ 103. It is guaranteed the the answer exists.

## Sample 1

Input

```text
3
```

Output

```text
1
```

## Sample 2

Input

```text
4
```

Output

```text
2
```

## Note

A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

For the first sample testcase, 3·1 + 1 = 4. We can output 1.

In the second sample testcase, 4·1 + 1 = 5. We cannot output 1 because 5 is prime. However, m = 2 is okay since 4·2 + 1 = 9, which is not a prime number.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
