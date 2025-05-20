# Doubly Linked List - Custom Palindrome Checker

## Problem Summary

Design a custom doubly linked list without using built-in data structures to check whether a sequence of characters forms a *custom palindrome*. A sequence is considered a custom palindrome if:
- It reads the same forwards and backwards,
- Ignores **case**,
- Ignores all **vowels** (`a, e, i, o, u`),
- Ignores **repeated characters** from both left and right.

## Approach Used

- **`node.py`**: Defines the `Node` class, representing each character in the list.
- **`DoublyLinkedList.py`**: Defines the `DoublyLinkedList` class with methods to:
  - Insert characters
  - Build cleaned sequences (left-to-right and right-to-left)
  - Check for custom palindrome
- **`main.py`**: Accepts user input, inserts characters into the list, and prints whether the sequence satisfies the custom palindrome rules.

The palindrome logic builds two cleaned sequences (one left-to-right, one right-to-left) and compares them for equality.

## Time & Space Complexity

| Operation               | Time Complexity  | Space Complexity |
|-------------------------|------------------|-------------------|
| insert(char)            | O(1)             | O(n)              |
| is_custom_palindrome()  | O(n²)*           | O(n)              |
| __str__                 | O(n)             | O(n)              |

\* Due to the use of a string to store "seen" characters and using `in` operator repeatedly (`O(n)` each time). Could be optimized with sets if allowed.

## Sample Test Cases

| Input      | Output |
|------------|--------|
| `Deified`  | True   |
| `ddoodd`   | True   |
| `banana`   | False  |
| `dood`     | True   |
| `Abba`     | True   |
| `bookkeeper` | False |

> Note: Sample outputs are based on strict enforcement of the three rules.

## Constraints

- Do not use built-in data structures like `list`, `deque`, `set`, or slicing.
- No use of `[::-1]`, `.reverse()`, or similar shortcuts.

## How to Run

1. Ensure all three files are in the same directory:
   - `node.py`
   - `DoublyLinkedList.py`
   - `main.py`

2. Run the program:

```bash
python main.py