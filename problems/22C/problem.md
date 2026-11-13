# 22C · System Administrator

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/22/C) · Rating 1700

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Bob got a job as a system administrator in X corporation. His first task was to connect n servers with the help of m two-way direct connection so that it becomes possible to transmit data from one server to any other server via these connections. Each direct connection has to link two different servers, each pair of servers should have at most one direct connection. Y corporation, a business rival of X corporation, made Bob an offer that he couldn't refuse: Bob was asked to connect the servers in such a way, that when server with index v fails, the transmission of data between some other two servers becomes impossible, i.e. the system stops being connected. Help Bob connect the servers.

## Input

The first input line contains 3 space-separated integer numbers n, m, v (3 ≤ n ≤ 105, 0 ≤ m ≤ 105, 1 ≤ v ≤ n), n — amount of servers, m — amount of direct connections, v — index of the server that fails and leads to the failure of the whole system.

## Output

If it is impossible to connect the servers in the required way, output -1. Otherwise output m lines with 2 numbers each — description of all the direct connections in the system. Each direct connection is described by two numbers — indexes of two servers, linked by this direct connection. The servers are numbered from 1. If the answer is not unique, output any.

## Sample 1

Input

```text
5 6 3
```

Output

```text
1 2
2 3
3 4
4 5
1 3
3 5
```

## Sample 2

Input

```text
6 100 1
```

Output

```text
-1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
