<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 491A · Up the hill

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/491/A) · Rating 1000

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Hiking club "Up the hill" just returned from a walk. Now they are trying to remember which hills they've just walked through.

It is known that there were N stops, all on different integer heights between 1 and N kilometers (inclusive) above the sea level. On the first day they've traveled from the first stop to the second stop, on the second day they've traveled from the second to the third and so on, and on the last day they've traveled from the stop N - 1 to the stop N and successfully finished their expedition.

They are trying to find out which heights were their stops located at. They have an entry in a travel journal specifying how many days did they travel up the hill, and how many days did they walk down the hill.

Help them by suggesting some possible stop heights satisfying numbers from the travel journal.

## Input

In the first line there is an integer non-negative number A denoting the number of days of climbing up the hill. Second line contains an integer non-negative number B — the number of days of walking down the hill (A + B + 1 = N, 1 ≤ N ≤ 100 000).

## Output

Output N space-separated distinct integers from 1 to N inclusive, denoting possible heights of the stops in order of visiting.

## Sample 1

Input

```text
0
1
```

Output

```text
2 1
```

## Sample 2

Input

```text
2
1
```

Output

```text
1 3 4 2
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
