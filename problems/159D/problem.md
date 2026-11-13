# 159D · Palindrome pairs

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">*special</span><span class="practice-tag">brute force</span><span class="practice-tag">dp</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/159/D) · Rating 1500

Time: 3.0 seconds · Memory: 256.0 MB

## Problem

You are given a non-empty string s consisting of lowercase letters. Find the number of pairs of non-overlapping palindromic substrings of this string.

In a more formal way, you have to find the quantity of tuples (a, b, x, y) such that 1 ≤ a ≤ b < x ≤ y ≤ |s| and substrings s[a... b], s[x... y] are palindromes.

A palindrome is a string that can be read the same way from left to right and from right to left. For example, "abacaba", "z", "abba" are palindromes.

A substring s[i... j] (1 ≤ i ≤ j ≤ |s|) of string s = s1s2... s|s| is a string sisi + 1... sj. For example, substring s[2...4] of string s = "abacaba" equals "bac".

## Input

The first line of input contains a non-empty string s which consists of lowercase letters ('a'...'z'), s contains at most 2000 characters.

## Output

Output a single number — the quantity of pairs of non-overlapping palindromic substrings of s.

Please do not use the %lld format specifier to read or write 64-bit integers in С++. It is preferred to use cin, cout streams or the %I64d format specifier.

## Sample 1

Input

```text
aa
```

Output

```text
1
```

## Sample 2

Input

```text
aaa
```

Output

```text
5
```

## Sample 3

Input

```text
abacaba
```

Output

```text
36
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
