<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 56C · Corporation Mail

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">data structures</span><span class="practice-tag">expression parsing</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/56/C) · Rating 1700

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The Beroil corporation structure is hierarchical, that is it can be represented as a tree. Let's examine the presentation of this structure as follows:

- employee ::= name. | name:employee1,employee2, ... ,employeek.
- name ::= name of an employee

That is, the description of each employee consists of his name, a colon (:), the descriptions of all his subordinates separated by commas, and, finally, a dot. If an employee has no subordinates, then the colon is not present in his description.

For example, line MIKE:MAX.,ARTEM:MIKE..,DMITRY:DMITRY.,DMITRY... is the correct way of recording the structure of a corporation where the director MIKE has subordinates MAX, ARTEM and DMITRY. ARTEM has a subordinate whose name is MIKE, just as the name of his boss and two subordinates of DMITRY are called DMITRY, just like himself.

In the Beroil corporation every employee can only correspond with his subordinates, at that the subordinates are not necessarily direct. Let's call an uncomfortable situation the situation when a person whose name is s writes a letter to another person whose name is also s. In the example given above are two such pairs: a pair involving MIKE, and two pairs for DMITRY (a pair for each of his subordinates).

Your task is by the given structure of the corporation to find the number of uncomfortable pairs in it.

## Input

The first and single line contains the corporation structure which is a string of length from 1 to 1000 characters. It is guaranteed that the description is correct. Every name is a string consisting of capital Latin letters from 1 to 10 symbols in length.

## Output

Print a single number — the number of uncomfortable situations in the company.

## Sample 1

Input

```text
MIKE:MAX.,ARTEM:MIKE..,DMITRY:DMITRY.,DMITRY...
```

Output

```text
3
```

## Sample 2

Input

```text
A:A..
```

Output

```text
1
```

## Sample 3

Input

```text
A:C:C:C:C.....
```

Output

```text
6
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
