# 344B · Simple Molecules

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">brute force</span><span class="practice-tag">graphs</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/344/B) · Rating 1200

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Mad scientist Mike is busy carrying out experiments in chemistry. Today he will attempt to join three atoms into one molecule.

A molecule consists of atoms, with some pairs of atoms connected by atomic bonds. Each atom has a valence number — the number of bonds the atom must form with other atoms. An atom can form one or multiple bonds with any other atom, but it cannot form a bond with itself. The number of bonds of an atom in the molecule must be equal to its valence number.

Mike knows valence numbers of the three atoms. Find a molecule that can be built from these atoms according to the stated rules, or determine that it is impossible.

## Input

The single line of the input contains three space-separated integers a, b and c (1 ≤ a, b, c ≤ 106) — the valence numbers of the given atoms.

## Output

If such a molecule can be built, print three space-separated integers — the number of bonds between the 1-st and the 2-nd, the 2-nd and the 3-rd, the 3-rd and the 1-st atoms, correspondingly. If there are multiple solutions, output any of them. If there is no solution, print "Impossible" (without the quotes).

## Sample 1

Input

```text
1 1 2
```

Output

```text
0 1 1
```

## Sample 2

Input

```text
3 4 5
```

Output

```text
1 3 2
```

## Sample 3

Input

```text
4 1 1
```

Output

```text
Impossible
```

## Note

The first sample corresponds to the first figure. There are no bonds between atoms 1 and 2 in this case.

The second sample corresponds to the second figure. There is one or more bonds between each pair of atoms.

The third sample corresponds to the third figure. There is no solution, because an atom cannot form bonds with itself.

The configuration in the fourth figure is impossible as each atom must have at least one atomic bond.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
