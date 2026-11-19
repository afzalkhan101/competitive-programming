<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 145B · Lucky Number 2

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/145/B) · Rating 1800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Petya loves lucky numbers very much. Everybody knows that lucky numbers are positive integers whose decimal record contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya loves long lucky numbers very much. He is interested in the minimum lucky number d that meets some condition. Let cnt(x) be the number of occurrences of number x in number d as a substring. For example, if d = 747747, then cnt(4) = 2, cnt(7) = 4, cnt(47) = 2, cnt(74) = 2. Petya wants the following condition to fulfil simultaneously: cnt(4) = a1, cnt(7) = a2, cnt(47) = a3, cnt(74) = a4. Petya is not interested in the occurrences of other numbers. Help him cope with this task.

## Input

The single line contains four integers a1, a2, a3 and a4 (1 ≤ a1, a2, a3, a4 ≤ 106).

## Output

On the single line print without leading zeroes the answer to the problem — the minimum lucky number d such, that cnt(4) = a1, cnt(7) = a2, cnt(47) = a3, cnt(74) = a4. If such number does not exist, print the single number "-1" (without the quotes).

## Sample 1

Input

```text
2 2 1 1
```

Output

```text
4774
```

## Sample 2

Input

```text
4 7 3 1
```

Output

```text
-1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
