<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 554A · Kyoya and Photobooks

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">math</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/554/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Kyoya Ootori is selling photobooks of the Ouran High School Host Club. He has 26 photos, labeled "a" to "z", and he has compiled them into a photo booklet with some photos in some order (possibly with some photos being duplicated). A photo booklet can be described as a string of lowercase letters, consisting of the photos in the booklet in order. He now wants to sell some "special edition" photobooks, each with one extra photo inserted anywhere in the book. He wants to make as many distinct photobooks as possible, so he can make more money. He asks Haruhi, how many distinct photobooks can he make by inserting one extra photo into the photobook he already has?

Please help Haruhi solve this problem.

## Input

The first line of input will be a single string s (1 ≤ |s| ≤ 20). String s consists only of lowercase English letters.

## Output

Output a single integer equal to the number of distinct photobooks Kyoya Ootori can make.

## Sample 1

Input

```text
a
```

Output

```text
51
```

## Sample 2

Input

```text
hi
```

Output

```text
76
```

## Note

In the first case, we can make 'ab','ac',...,'az','ba','ca',...,'za', and 'aa', producing a total of 51 distinct photo booklets.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
