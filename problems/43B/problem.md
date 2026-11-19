<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 43B · Letter

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/43/B) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vasya decided to write an anonymous letter cutting the letters out of a newspaper heading. He knows heading s1 and text s2 that he wants to send. Vasya can use every single heading letter no more than once. Vasya doesn't have to cut the spaces out of the heading — he just leaves some blank space to mark them. Help him; find out if he will manage to compose the needed text.

## Input

The first line contains a newspaper heading s1. The second line contains the letter text s2. s1 и s2 are non-empty lines consisting of spaces, uppercase and lowercase Latin letters, whose lengths do not exceed 200 symbols. The uppercase and lowercase letters should be differentiated. Vasya does not cut spaces out of the heading.

## Output

If Vasya can write the given anonymous letter, print YES, otherwise print NO

## Sample 1

Input

```text
Instead of dogging Your footsteps it disappears but you dont notice anything
where is your dog
```

Output

```text
NO
```

## Sample 2

Input

```text
Instead of dogging Your footsteps it disappears but you dont notice anything
Your dog is upstears
```

Output

```text
YES
```

## Sample 3

Input

```text
Instead of dogging your footsteps it disappears but you dont notice anything
Your dog is upstears
```

Output

```text
NO
```

## Sample 4

Input

```text
abcdefg hijk
k j i h g f e d c b a
```

Output

```text
YES
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
