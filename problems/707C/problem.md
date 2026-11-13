# 707C · Pythagorean Triples

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/707/C) · Rating 1500

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Katya studies in a fifth grade. Recently her class studied right triangles and the Pythagorean theorem. It appeared, that there are triples of positive integers such that you can construct a right triangle with segments of lengths corresponding to triple. Such triples are called Pythagorean triples.

For example, triples (3, 4, 5), (5, 12, 13) and (6, 8, 10) are Pythagorean triples.

Here Katya wondered if she can specify the length of some side of right triangle and find any Pythagorean triple corresponding to such length? Note that the side which length is specified can be a cathetus as well as hypotenuse.

Katya had no problems with completing this task. Will you do the same?

## Input

The only line of the input contains single integer n (1 ≤ n ≤ 109) — the length of some side of a right triangle.

## Output

Print two integers m and k (1 ≤ m, k ≤ 1018), such that n, m and k form a Pythagorean triple, in the only line.

In case if there is no any Pythagorean triple containing integer n, print  - 1 in the only line. If there are many answers, print any of them.

## Sample 1

Input

```text
3
```

Output

```text
4 5
```

## Sample 2

Input

```text
6
```

Output

```text
8 10
```

## Sample 3

Input

```text
1
```

Output

```text
-1
```

## Sample 4

Input

```text
17
```

Output

```text
144 145
```

## Sample 5

Input

```text
67
```

Output

```text
2244 2245
```

## Note

Illustration for the first sample.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
