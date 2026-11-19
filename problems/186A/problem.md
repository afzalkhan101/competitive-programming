<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 186A · Comparing Strings

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/186/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Some dwarves that are finishing the StUDY (State University for Dwarven Youngsters) Bachelor courses, have been told "no genome, no degree". That means that all dwarves should write a thesis on genome. Dwarven genome is far from simple. It is represented by a string that consists of lowercase Latin letters.

Dwarf Misha has already chosen the subject for his thesis: determining by two dwarven genomes, whether they belong to the same race. Two dwarves belong to the same race if we can swap two characters in the first dwarf's genome and get the second dwarf's genome as a result. Help Dwarf Misha and find out whether two gnomes belong to the same race or not.

## Input

The first line contains the first dwarf's genome: a non-empty string, consisting of lowercase Latin letters.

The second line contains the second dwarf's genome: a non-empty string, consisting of lowercase Latin letters.

The number of letters in each genome doesn't exceed 105. It is guaranteed that the strings that correspond to the genomes are different. The given genomes may have different length.

## Output

Print "YES", if the dwarves belong to the same race. Otherwise, print "NO".

## Sample 1

Input

```text
ab
ba
```

Output

```text
YES
```

## Sample 2

Input

```text
aa
ab
```

Output

```text
NO
```

## Note

- First example: you can simply swap two letters in string "ab". So we get "ba".
- Second example: we can't change string "aa" into string "ab", because "aa" does not contain letter "b".

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
