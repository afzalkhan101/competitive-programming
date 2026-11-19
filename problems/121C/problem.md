<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 121C · Lucky Permutation

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">combinatorics</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/121/C) · Rating 1900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

One day Petya dreamt of a lexicographically k-th permutation of integers from 1 to n. Determine how many lucky numbers in the permutation are located on the positions whose indexes are also lucky numbers.

## Input

The first line contains two integers n and k (1 ≤ n, k ≤ 109) — the number of elements in the permutation and the lexicographical number of the permutation.

## Output

If the k-th permutation of numbers from 1 to n does not exist, print the single number "-1" (without the quotes). Otherwise, print the answer to the problem: the number of such indexes i, that i and ai are both lucky numbers.

## Sample 1

Input

```text
7 4
```

Output

```text
1
```

## Sample 2

Input

```text
4 7
```

Output

```text
1
```

## Note

A permutation is an ordered set of n elements, where each integer from 1 to n occurs exactly once. The element of permutation in position with index i is denoted as ai (1 ≤ i ≤ n). Permutation a is lexicographically smaller that permutation b if there is such a i (1 ≤ i ≤ n), that ai < bi, and for any j (1 ≤ j < i) aj = bj. Let's make a list of all possible permutations of n elements and sort it in the order of lexicographical increasing. Then the lexicographically k-th permutation is the k-th element of this list of permutations.

In the first sample the permutation looks like that:

1 2 3 4 6 7 5

The only suitable position is 4.

In the second sample the permutation looks like that:

2 1 3 4

The only suitable position is 4.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
