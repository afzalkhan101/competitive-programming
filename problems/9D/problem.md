# 9D · How many trees?

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">combinatorics</span><span class="practice-tag">divide and conquer</span><span class="practice-tag">dp</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/9/D) · Rating 1900

Time: 1.0 seconds · Memory: 64.0 MB

## Problem

In one very old text file there was written Great Wisdom. This Wisdom was so Great that nobody could decipher it, even Phong — the oldest among the inhabitants of Mainframe. But still he managed to get some information from there. For example, he managed to learn that User launches games for pleasure — and then terrible Game Cubes fall down on the city, bringing death to those modules, who cannot win the game...

For sure, as guard Bob appeared in Mainframe many modules stopped fearing Game Cubes. Because Bob (as he is alive yet) has never been defeated by User, and he always meddles with Game Cubes, because he is programmed to this.

However, unpleasant situations can happen, when a Game Cube falls down on Lost Angles. Because there lives a nasty virus — Hexadecimal, who is... mmm... very strange. And she likes to play very much. So, willy-nilly, Bob has to play with her first, and then with User.

This time Hexadecimal invented the following entertainment: Bob has to leap over binary search trees with n nodes. We should remind you that a binary search tree is a binary tree, each node has a distinct key, for each node the following is true: the left sub-tree of a node contains only nodes with keys less than the node's key, the right sub-tree of a node contains only nodes with keys greater than the node's key. All the keys are different positive integer numbers from 1 to n. Each node of such a tree can have up to two children, or have no children at all (in the case when a node is a leaf).

In Hexadecimal's game all the trees are different, but the height of each is not lower than h. In this problem «height» stands for the maximum amount of nodes on the way from the root to the remotest leaf, the root node and the leaf itself included. When Bob leaps over a tree, it disappears. Bob gets the access to a Cube, when there are no trees left. He knows how many trees he will have to leap over in the worst case. And you?

## Input

The input data contains two space-separated positive integer numbers n and h (n ≤ 35, h ≤ n).

## Output

Output one number — the answer to the problem. It is guaranteed that it does not exceed 9·1018.

## Sample 1

Input

```text
3 2
```

Output

```text
5
```

## Sample 2

Input

```text
3 3
```

Output

```text
4
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
