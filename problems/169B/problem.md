# 169B · Replacing Digits

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/169/B) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You are given an integer a that consists of n digits. You are also given a sequence of digits s of length m. The digit in position j (1 ≤ j ≤ m) of sequence s means that you can choose an arbitrary position i (1 ≤ i ≤ n) in a and replace the digit in the chosen position i with sj. Each element in the sequence s can participate in no more than one replacing operation.

Your task is to perform such sequence of replacements, that the given number a gets maximum value. You are allowed to use not all elements from s.

## Input

The first line contains positive integer a. Its length n is positive and doesn't exceed 105. The second line contains sequence of digits s. Its length m is positive and doesn't exceed 105. The digits in the sequence s are written consecutively without any separators.

The given number a doesn't contain leading zeroes.

## Output

Print the maximum value that can be obtained from a after a series of replacements. You are allowed to use not all elements from s. The printed number shouldn't contain any leading zeroes.

## Sample 1

Input

```text
1024
010
```

Output

```text
1124
```

## Sample 2

Input

```text
987
1234567
```

Output

```text
987
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
