# 53A · Autocomplete

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/53/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Autocomplete is a program function that enables inputting the text (in editors, command line shells, browsers etc.) completing the text by its inputted part. Vasya is busy working on a new browser called 'BERowser'. He happens to be working on the autocomplete function in the address line at this very moment. A list consisting of n last visited by the user pages and the inputted part s are known. Your task is to complete s to make it an address of one of the pages from the list. You have to find the lexicographically smallest address having a prefix s.

## Input

The first line contains the s line which is the inputted part. The second line contains an integer n (1 ≤ n ≤ 100) which is the number of visited pages. Then follow n lines which are the visited pages, one on each line. All the lines have lengths of from 1 to 100 symbols inclusively and consist of lowercase Latin letters only.

## Output

If s is not the beginning of any of n addresses of the visited pages, print s. Otherwise, print the lexicographically minimal address of one of the visited pages starting from s.

The lexicographical order is the order of words in a dictionary. The lexicographical comparison of lines is realized by the '<' operator in the modern programming languages.

## Sample 1

Input

```text
next
2
nextpermutation
nextelement
```

Output

```text
nextelement
```

## Sample 2

Input

```text
find
4
find
findfirstof
findit
fand
```

Output

```text
find
```

## Sample 3

Input

```text
find
4
fondfind
fondfirstof
fondit
fand
```

Output

```text
find
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
