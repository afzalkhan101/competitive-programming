# 113A · Grammar Lessons

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/113/A) · Rating 1600

Time: 5.0 seconds · Memory: 256.0 MB

## Problem

Petya got interested in grammar on his third year in school. He invented his own language called Petya's. Petya wanted to create a maximally simple language that would be enough to chat with friends, that's why all the language's grammar can be described with the following set of rules:

- There are three parts of speech: the adjective, the noun, the verb. Each word in his language is an adjective, noun or verb.
- There are two genders: masculine and feminine. Each word in his language has gender either masculine or feminine.
- Masculine adjectives end with -lios, and feminine adjectives end with -liala.
- Masculine nouns end with -etr, and feminime nouns end with -etra.
- Masculine verbs end with -initis, and feminime verbs end with -inites.
- Thus, each word in the Petya's language has one of the six endings, given above. There are no other endings in Petya's language.
- It is accepted that the whole word consists of an ending. That is, words "lios", "liala", "etr" and so on belong to the Petya's language.
- There aren't any punctuation marks, grammatical tenses, singular/plural forms or other language complications.
- A sentence is either exactly one valid language word or exactly one statement.

Statement is any sequence of the Petya's language, that satisfy both conditions:

- Words in statement follow in the following order (from the left to the right): zero or more adjectives followed by exactly one noun followed by zero or more verbs.
- All words in the statement should have the same gender.

After Petya's friend Vasya wrote instant messenger (an instant messaging program) that supported the Petya's language, Petya wanted to add spelling and grammar checking to the program. As Vasya was in the country and Petya didn't feel like waiting, he asked you to help him with this problem. Your task is to define by a given sequence of words, whether it is true that the given text represents exactly one sentence in Petya's language.

## Input

The first line contains one or more words consisting of lowercase Latin letters. The overall number of characters (including letters and spaces) does not exceed 105.

It is guaranteed that any two consecutive words are separated by exactly one space and the input data do not contain any other spaces. It is possible that given words do not belong to the Petya's language.

## Output

If some word of the given text does not belong to the Petya's language or if the text contains more that one sentence, print "NO" (without the quotes). Otherwise, print "YES" (without the quotes).

## Sample 1

Input

```text
petr
```

Output

```text
YES
```

## Sample 2

Input

```text
etis atis animatis etis atis amatis
```

Output

```text
NO
```

## Sample 3

Input

```text
nataliala kataliala vetra feinites
```

Output

```text
YES
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
