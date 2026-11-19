<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 452A · Eevee

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/452/A) · Rating 1000

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

You are solving the crossword problem K from IPSC 2014. You solved all the clues except for one: who does Eevee evolve into? You are not very into pokemons, but quick googling helped you find out, that Eevee can evolve into eight different pokemons: Vaporeon, Jolteon, Flareon, Espeon, Umbreon, Leafeon, Glaceon, and Sylveon.

You know the length of the word in the crossword, and you already know some letters. Designers of the crossword made sure that the answer is unambiguous, so you can assume that exactly one pokemon out of the 8 that Eevee evolves into fits the length and the letters given. Your task is to find it.

## Input

First line contains an integer n (6 ≤ n ≤ 8) – the length of the string.

Next line contains a string consisting of n characters, each of which is either a lower case english letter (indicating a known letter) or a dot character (indicating an empty cell in the crossword).

## Output

Print a name of the pokemon that Eevee can evolve into that matches the pattern in the input. Use lower case letters only to print the name (in particular, do not capitalize the first letter).

## Sample 1

Input

```text
7
j......
```

Output

```text
jolteon
```

## Sample 2

Input

```text
7
...feon
```

Output

```text
leafeon
```

## Sample 3

Input

```text
7
.l.r.o.
```

Output

```text
flareon
```

## Note

Here's a set of names in a form you can paste into your solution:

["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]

{"vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"}

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
