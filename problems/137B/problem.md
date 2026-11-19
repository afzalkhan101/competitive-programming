<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 137B · Permutation

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/137/B) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

"Hey, it's homework time" — thought Polycarpus and of course he started with his favourite subject, IT. Polycarpus managed to solve all tasks but for the last one in 20 minutes. However, as he failed to solve the last task after some considerable time, the boy asked you to help him.

The sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

You are given an arbitrary sequence a1, a2, ..., an containing n integers. Each integer is not less than 1 and not greater than 5000. Determine what minimum number of elements Polycarpus needs to change to get a permutation (he should not delete or add numbers). In a single change he can modify any single sequence element (i. e. replace it with another integer).

## Input

The first line of the input data contains an integer n (1 ≤ n ≤ 5000) which represents how many numbers are in the sequence. The second line contains a sequence of integers ai (1 ≤ ai ≤ 5000, 1 ≤ i ≤ n).

## Output

Print the only number — the minimum number of changes needed to get the permutation.

## Sample 1

Input

```text
3
3 1 2
```

Output

```text
0
```

## Sample 2

Input

```text
2
2 2
```

Output

```text
1
```

## Sample 3

Input

```text
5
5 3 3 3 1
```

Output

```text
2
```

## Note

The first sample contains the permutation, which is why no replacements are required.

In the second sample it is enough to replace the first element with the number 1 and that will make the sequence the needed permutation.

In the third sample we can replace the second element with number 4 and the fourth element with number 2.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
