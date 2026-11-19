<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 106B · Choosing Laptop

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">brute force</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/106/B) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vasya is choosing a laptop. The shop has n laptops to all tastes.

Vasya is interested in the following properties: processor speed, ram and hdd. Vasya is a programmer and not a gamer which is why he is not interested in all other properties.

If all three properties of a laptop are strictly less than those properties of some other laptop, then the first laptop is considered outdated by Vasya. Among all laptops Vasya does not consider outdated, he chooses the cheapest one.

There are very many laptops, which is why Vasya decided to write a program that chooses the suitable laptop. However, Vasya doesn't have his own laptop yet and he asks you to help him.

## Input

The first line contains number n (1 ≤ n ≤ 100).

Then follow n lines. Each describes a laptop as speed ram hdd cost. Besides,

- speed, ram, hdd and cost are integers
- 1000 ≤ speed ≤ 4200 is the processor's speed in megahertz
- 256 ≤ ram ≤ 4096 the RAM volume in megabytes
- 1 ≤ hdd ≤ 500 is the HDD in gigabytes
- 100 ≤ cost ≤ 1000 is price in tugriks

All laptops have different prices.

## Output

Print a single number — the number of a laptop Vasya will choose. The laptops are numbered with positive integers from 1 to n in the order in which they are given in the input data.

## Sample 1

Input

```text
5
2100 512 150 200
2000 2048 240 350
2300 1024 200 320
2500 2048 80 300
2000 512 180 150
```

Output

```text
4
```

## Note

In the third sample Vasya considers the first and fifth laptops outdated as all of their properties cannot match those of the third laptop. The fourth one is the cheapest among the laptops that are left. Thus, Vasya chooses the fourth laptop.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
