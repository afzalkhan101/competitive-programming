# 46C · Hamsters and Tigers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">two pointers</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/46/C) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Today there is going to be an unusual performance at the circus — hamsters and tigers will perform together! All of them stand in circle along the arena edge and now the trainer faces a difficult task: he wants to swap the animals' positions so that all the hamsters stood together and all the tigers also stood together. The trainer swaps the animals in pairs not to create a mess. He orders two animals to step out of the circle and swap places. As hamsters feel highly uncomfortable when tigers are nearby as well as tigers get nervous when there's so much potential prey around (consisting not only of hamsters but also of yummier spectators), the trainer wants to spend as little time as possible moving the animals, i.e. he wants to achieve it with the minimal number of swaps. Your task is to help him.

## Input

The first line contains number n (2 ≤ n ≤ 1000) which indicates the total number of animals in the arena. The second line contains the description of the animals' positions. The line consists of n symbols "H" and "T". The "H"s correspond to hamsters and the "T"s correspond to tigers. It is guaranteed that at least one hamster and one tiger are present on the arena. The animals are given in the order in which they are located circle-wise, in addition, the last animal stands near the first one.

## Output

Print the single number which is the minimal number of swaps that let the trainer to achieve his goal.

## Sample 1

Input

```text
3
HTH
```

Output

```text
0
```

## Sample 2

Input

```text
9
HTHTHTHHT
```

Output

```text
2
```

## Note

In the first example we shouldn't move anybody because the animals of each species already stand apart from the other species. In the second example you may swap, for example, the tiger in position 2 with the hamster in position 5 and then — the tiger in position 9 with the hamster in position 7.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
