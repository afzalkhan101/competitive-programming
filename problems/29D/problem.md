<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 29D · Ant on the Tree

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">trees</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/29/D) · Rating 2000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Connected undirected graph without cycles is called a tree. Trees is a class of graphs which is interesting not only for people, but for ants too.

An ant stands at the root of some tree. He sees that there are n vertexes in the tree, and they are connected by n - 1 edges so that there is a path between any pair of vertexes. A leaf is a distinct from root vertex, which is connected with exactly one other vertex.

The ant wants to visit every vertex in the tree and return to the root, passing every edge twice. In addition, he wants to visit the leaves in a specific order. You are to find some possible route of the ant.

## Input

The first line contains integer n (3 ≤ n ≤ 300) — amount of vertexes in the tree. Next n - 1 lines describe edges. Each edge is described with two integers — indexes of vertexes which it connects. Each edge can be passed in any direction. Vertexes are numbered starting from 1. The root of the tree has number 1. The last line contains k integers, where k is amount of leaves in the tree. These numbers describe the order in which the leaves should be visited. It is guaranteed that each leaf appears in this order exactly once.

## Output

If the required route doesn't exist, output -1. Otherwise, output 2n - 1 numbers, describing the route. Every time the ant comes to a vertex, output it's index.

## Sample 1

Input

```text
3
1 2
2 3
3
```

Output

```text
1 2 3 2 1
```

## Sample 2

Input

```text
6
1 2
1 3
2 4
4 5
4 6
5 6 3
```

Output

```text
1 2 4 5 4 6 4 2 1 3 1
```

## Sample 3

Input

```text
6
1 2
1 3
2 4
4 5
4 6
5 3 6
```

Output

```text
-1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
