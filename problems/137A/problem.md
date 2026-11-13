# 137A · Postcards and photos

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/137/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Polycarpus has postcards and photos hung in a row on the wall. He decided to put them away to the closet and hang on the wall a famous painter's picture. Polycarpus does it like that: he goes from the left to the right and removes the objects consecutively. As Polycarpus doesn't want any mix-ups to happen, he will not carry in his hands objects of two different types. In other words, Polycarpus can't carry both postcards and photos simultaneously. Sometimes he goes to the closet and puts the objects there, thus leaving his hands free. Polycarpus must put all the postcards and photos to the closet. He cannot skip objects. What minimum number of times he should visit the closet if he cannot carry more than 5 items?

## Input

The only line of the input data contains a non-empty string consisting of letters "С" and "P" whose length does not exceed 100 characters. If the i-th character in the string is the letter "С", that means that the i-th object (the numbering goes from the left to the right) on Polycarpus' wall is a postcard. And if the i-th character is the letter "P", than the i-th object on the wall is a photo.

## Output

Print the only number — the minimum number of times Polycarpus has to visit the closet.

## Sample 1

Input

```text
CPCPCPC
```

Output

```text
7
```

## Sample 2

Input

```text
CCCCCCPPPPPP
```

Output

```text
4
```

## Sample 3

Input

```text
CCCCCCPPCPPPPPPPPPP
```

Output

```text
6
```

## Sample 4

Input

```text
CCCCCCCCCC
```

Output

```text
2
```

## Note

In the first sample Polycarpus needs to take one item to the closet 7 times.

In the second sample Polycarpus can first take 3 postcards to the closet; then 3 more. He can take the 6 photos that are left in the similar way, going to the closet twice.

In the third sample Polycarpus can visit the closet twice, both times carrying 3 postcards. Then he can take there 2 photos at once, then one postcard and finally, he can carry the last 10 photos if he visits the closet twice.

In the fourth sample Polycarpus can visit the closet twice and take there all 10 postcards (5 items during each go).

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
