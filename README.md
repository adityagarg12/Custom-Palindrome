# Doubly Linked List - Custom Palindrome Checker

## 🔍 Problem Summary

Design a custom doubly linked list without using built-in data structures to check whether a sequence of characters forms a *custom palindrome*. A sequence is considered a custom palindrome if:
- It reads the same forwards and backwards,
- Ignores **case**,
- Ignores all **vowels** (`a, e, i, o, u`),
- Ignores **repeated characters** from both left and right.

## 🧠 Approach Used

- A `Node` class is defined for each character in the list.
- A `DoublyLinkedList` class manages insertion and traversal of characters.
- During palindrome check:
  - Two cleaned strings are built:
    - One from **left to right**
    - One from **right to left**
  - While building, the algorithm:
    - Converts characters to lowercase
    - Skips vowels
    - Skips characters already seen in that direction
- If both cleaned sequences are equal, the sequence is a custom palindrome.

## ⏱️ Time & Space Complexity

| Operation               | Time Complexity  | Space Complexity |
|-------------------------|------------------|-------------------|
| insert(char)            | O(1)             | O(n)              |
| is_custom_palindrome()  | O(n²)*           | O(n)              |
| __str__                 | O(n)             | O(n)              |

\* Due to the use of a string to store "seen" characters and using `in` operator repeatedly (`O(n)` each time). Could be optimized with sets if allowed.

## 🧪 Sample Test Cases

| Input      | Output |
|------------|--------|
| `Deified`  | True   |
| `ddoodd`   | True   |
| `banana`   | False  |
| `dood`     | True   |
| `Abba`     | True   |
| `bookkeeper` | False |

> Note: Sample outputs are based on strict enforcement of the three rules.

## 🚫 Constraints

- Do not use built-in data structures like `list`, `deque`, `set`, or slicing.
- No use of `[::-1]`, `.reverse()`, or similar shortcuts.
