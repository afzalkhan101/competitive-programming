# 41A · Translation

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/41/A) · Rating 800

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

The translation from the Berland language into the Birland language is not an easy task. Those languages are very similar: a Berlandish word differs from a Birlandish word with the same meaning a little: it is spelled (and pronounced) reversely. For example, a Berlandish word code corresponds to a Birlandish word edoc. However, making a mistake during the "translation" is easy. Vasya translated the word s from Berlandish into Birlandish as t. Help him: find out if he translated the word correctly.

## Input

The first line contains word s, the second line contains word t. The words consist of lowercase Latin letters. The input data do not contain unnecessary spaces. The words are not empty and their lengths do not exceed 100 symbols.

## Output

If the word t is a word s, written reversely, print YES, otherwise print NO.

## Sample 1

Input

```text
code
edoc
```

Output

```text
YES
```

## Sample 2

Input

```text
abb
aba
```

Output

```text
NO
```

## Sample 3

Input

```text
code
code
```

Output

```text
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
