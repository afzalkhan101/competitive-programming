<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 94B · Friends

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">graphs</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/94/B) · Rating 1300

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

One day Igor K. stopped programming and took up math. One late autumn evening he was sitting at a table reading a book and thinking about something.

The following statement caught his attention: "Among any six people there are either three pairwise acquainted people or three pairwise unacquainted people"

Igor just couldn't get why the required minimum is 6 people. "Well, that's the same for five people, too!" — he kept on repeating in his mind. — "Let's take, say, Max, Ilya, Vova — here, they all know each other! And now let's add Dima and Oleg to Vova — none of them is acquainted with each other! Now, that math is just rubbish!"

Igor K. took 5 friends of his and wrote down who of them is friends with whom. Now he wants to check whether it is true for the five people that among them there are either three pairwise acquainted or three pairwise not acquainted people.

## Input

The first line contains an integer m (0 ≤ m ≤ 10), which is the number of relations of acquaintances among the five friends of Igor's.

Each of the following m lines contains two integers ai and bi (1 ≤ ai, bi ≤ 5;ai ≠ bi), where (ai, bi) is a pair of acquainted people. It is guaranteed that each pair of the acquaintances is described exactly once. The acquaintance relation is symmetrical, i.e. if x is acquainted with y, then y is also acquainted with x.

## Output

Print "FAIL", if among those five people there are no either three pairwise acquainted or three pairwise unacquainted people. Otherwise print "WIN".

## Sample 1

Input

```text
4
1 3
2 3
1 4
5 3
```

Output

```text
WIN
```

## Sample 2

Input

```text
5
1 2
2 3
3 4
4 5
5 1
```

Output

```text
FAIL
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
