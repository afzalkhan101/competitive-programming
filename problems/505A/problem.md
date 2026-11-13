# 505A · Mr. Kitayuta's Gift

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/505/A) · Rating 1100

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Mr. Kitayuta has kindly given you a string s consisting of lowercase English letters. You are asked to insert exactly one lowercase English letter into s to make it a palindrome. A palindrome is a string that reads the same forward and backward. For example, "noon", "testset" and "a" are all palindromes, while "test" and "kitayuta" are not.

You can choose any lowercase English letter, and insert it to any position of s, possibly to the beginning or the end of s. You have to insert a letter even if the given string is already a palindrome.

If it is possible to insert one lowercase English letter into s so that the resulting string will be a palindrome, print the string after the insertion. Otherwise, print "NA" (without quotes, case-sensitive). In case there is more than one palindrome that can be obtained, you are allowed to print any of them.

## Input

The only line of the input contains a string s (1 ≤ |s| ≤ 10). Each character in s is a lowercase English letter.

## Output

If it is possible to turn s into a palindrome by inserting one lowercase English letter, print the resulting string in a single line. Otherwise, print "NA" (without quotes, case-sensitive). In case there is more than one solution, any of them will be accepted.

## Sample 1

Input

```text
revive
```

Output

```text
reviver
```

## Sample 2

Input

```text
ee
```

Output

```text
eye
```

## Sample 3

Input

```text
kitayuta
```

Output

```text
NA
```

## Note

For the first sample, insert 'r' to the end of "revive" to obtain a palindrome "reviver".

For the second sample, there is more than one solution. For example, "eve" will also be accepted.

For the third sample, it is not possible to turn "kitayuta" into a palindrome by just inserting one letter.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
