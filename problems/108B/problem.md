<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 108B · Datatypes

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">math</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/108/B) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Tattah's youngest brother, Tuftuf, is new to programming.

Since his older brother is such a good programmer, his biggest dream is to outshine him. Tuftuf is a student at the German University in Cairo (GUC) where he learns to write programs in Gava.

Today, Tuftuf was introduced to Gava's unsigned integer datatypes. Gava has n unsigned integer datatypes of sizes (in bits) a1, a2, ... an. The i-th datatype have size ai bits, so it can represent every integer between 0 and 2ai - 1 inclusive.

Tuftuf is thinking of learning a better programming language. If there exists an integer x, such that x fits in some type i (in ai bits) and x·x does not fit in some other type j (in aj bits) where ai < aj, then Tuftuf will stop using Gava.

Your task is to determine Tuftuf's destiny.

## Input

The first line contains integer n (2 ≤ n ≤ 105) — the number of Gava's unsigned integer datatypes' sizes. The second line contains a single-space-separated list of n integers (1 ≤ ai ≤ 109) — sizes of datatypes in bits. Some datatypes may have equal sizes.

## Output

Print "YES" if Tuftuf will stop using Gava, and "NO" otherwise.

## Sample 1

Input

```text
3
64 16 32
```

Output

```text
NO
```

## Sample 2

Input

```text
4
4 2 1 3
```

Output

```text
YES
```

## Note

In the second example, x = 7 (1112) fits in 3 bits, but x2 = 49 (1100012) does not fit in 4 bits.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
