# 66B · Petya and Countryside

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">brute force</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/66/B) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Little Petya often travels to his grandmother in the countryside. The grandmother has a large garden, which can be represented as a rectangle 1 × n in size, when viewed from above. This rectangle is divided into n equal square sections. The garden is very unusual as each of the square sections possesses its own fixed height and due to the newest irrigation system we can create artificial rain above each section.

Creating artificial rain is an expensive operation. That's why we limit ourselves to creating the artificial rain only above one section. At that, the water from each watered section will flow into its neighbouring sections if their height does not exceed the height of the section. That is, for example, the garden can be represented by a 1 × 5 rectangle, where the section heights are equal to 4, 2, 3, 3, 2. Then if we create an artificial rain over any of the sections with the height of 3, the water will flow over all the sections, except the ones with the height of 4. See the illustration of this example at the picture:

As Petya is keen on programming, he decided to find such a section that if we create artificial rain above it, the number of watered sections will be maximal. Help him.

## Input

The first line contains a positive integer n (1 ≤ n ≤ 1000). The second line contains n positive integers which are the height of the sections. All the numbers are no less than 1 and not more than 1000.

## Output

Print a single number, the maximal number of watered sections if we create artificial rain above exactly one section.

## Sample 1

Input

```text
1
2
```

Output

```text
1
```

## Sample 2

Input

```text
5
1 2 1 2 1
```

Output

```text
3
```

## Sample 3

Input

```text
8
1 2 1 1 1 3 3 4
```

Output

```text
6
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
