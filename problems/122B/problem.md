<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 122B · Lucky Substring

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">brute force</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/122/B) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

One day Petya was delivered a string s, containing only digits. He needs to find a string that

- represents a lucky number without leading zeroes,
- is not empty,
- is contained in s as a substring the maximum number of times.

Among all the strings for which the three conditions given above are fulfilled, Petya only needs the lexicographically minimum one. Find this string for Petya.

## Input

The single line contains a non-empty string s whose length can range from 1 to 50, inclusive. The string only contains digits. The string can contain leading zeroes.

## Output

In the only line print the answer to Petya's problem. If the sought string does not exist, print "-1" (without quotes).

## Sample 1

Input

```text
047
```

Output

```text
4
```

## Sample 2

Input

```text
16
```

Output

```text
-1
```

## Sample 3

Input

```text
472747
```

Output

```text
7
```

## Note

The lexicographical comparison of strings is performed by the < operator in the modern programming languages. String x is lexicographically less than string y either if x is a prefix of y, or exists such i (1 ≤ i ≤ min(|x|, |y|)), that xi < yi and for any j (1 ≤ j < i) xj = yj. Here |a| denotes the length of string a.

In the first sample three conditions are fulfilled for strings "4", "7" and "47". The lexicographically minimum one is "4".

In the second sample s has no substrings which are lucky numbers.

In the third sample the three conditions are only fulfilled for string "7".

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
