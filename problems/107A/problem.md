<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 107A · Dorm Water Supply

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/107/A) · Rating 1400

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

The German University in Cairo (GUC) dorm houses are numbered from 1 to n. Underground water pipes connect these houses together. Each pipe has certain direction (water can flow only in this direction and not vice versa), and diameter (which characterizes the maximal amount of water it can handle).

For each house, there is at most one pipe going into it and at most one pipe going out of it. With the new semester starting, GUC student and dorm resident, Lulu, wants to install tanks and taps at the dorms. For every house with an outgoing water pipe and without an incoming water pipe, Lulu should install a water tank at that house. For every house with an incoming water pipe and without an outgoing water pipe, Lulu should install a water tap at that house. Each tank house will convey water to all houses that have a sequence of pipes from the tank to it. Accordingly, each tap house will receive water originating from some tank house.

In order to avoid pipes from bursting one week later (like what happened last semester), Lulu also has to consider the diameter of the pipes. The amount of water each tank conveys should not exceed the diameter of the pipes connecting a tank to its corresponding tap. Lulu wants to find the maximal amount of water that can be safely conveyed from each tank to its corresponding tap.

## Input

The first line contains two space-separated integers n and p (1 ≤ n ≤ 1000, 0 ≤ p ≤ n) — the number of houses and the number of pipes correspondingly.

Then p lines follow — the description of p pipes. The i-th line contains three integers ai bi di, indicating a pipe of diameter di going from house ai to house bi (1 ≤ ai, bi ≤ n, ai ≠ bi, 1 ≤ di ≤ 106).

It is guaranteed that for each house there is at most one pipe going into it and at most one pipe going out of it.

## Output

Print integer t in the first line — the number of tank-tap pairs of houses.

For the next t lines, print 3 integers per line, separated by spaces: tanki, tapi, and diameteri, where tanki ≠ tapi (1 ≤ i ≤ t). Here tanki and tapi are indexes of tank and tap houses respectively, and diameteri is the maximum amount of water that can be conveyed. All the t lines should be ordered (increasingly) by tanki.

## Sample 1

Input

```text
3 2
1 2 10
2 3 20
```

Output

```text
1
1 3 10
```

## Sample 2

Input

```text
3 3
1 2 20
2 3 10
3 1 5
```

Output

```text
0
```

## Sample 3

Input

```text
4 2
1 2 60
3 4 50
```

Output

```text
2
1 2 60
3 4 50
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
