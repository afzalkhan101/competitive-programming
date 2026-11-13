# 96B · Lucky Numbers (easy)

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">binary search</span><span class="practice-tag">bitmasks</span><span class="practice-tag">brute force</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/96/B) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Petya loves lucky numbers. Everybody knows that positive integers are lucky if their decimal representation doesn't contain digits other than 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Lucky number is super lucky if it's decimal representation contains equal amount of digits 4 and 7. For example, numbers 47, 7744, 474477 are super lucky and 4, 744, 467 are not.

One day Petya came across a positive integer n. Help him to find the least super lucky number which is not less than n.

## Input

The only line contains a positive integer n (1 ≤ n ≤ 109). This number doesn't have leading zeroes.

## Output

Output the least super lucky number that is more than or equal to n.

Please, do not use the %lld specificator to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specificator.

## Sample 1

Input

```text
4500
```

Output

```text
4747
```

## Sample 2

Input

```text
47
```

Output

```text
47
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
