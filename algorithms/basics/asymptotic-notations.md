# Asymptotic Notations
## What is asymptotic notation?
Is a mathematical tool to measure the **time complexity of a function** given certain input, so we can know his **runtime**.
## What notations we have?
We have three types of notations:
- **Big-O notation**: It's a notation that shows the worst-case scenario of a function. For example, in [[bubble-sort]], the worst case happens when the array is ordered in descendent order. Then, the Big-O of bubble-sort is n².
- **Omega Notation**: This notation shows the best case scenario of a a function. For example, in bubble-sort, the best case scenario when the array is already sorted. So, the Omega of bubble-sort is n.
- **Theta Notation**: Is used to describe the average case of a function. In the case of bubble-sort, his Theta is n², equal to his Big-O.

## Common runtimes
This are the most-common runtimes of algorithms with an example, sorted by efficiency. In asymptotic notation, the runtimes are simplified, because is massive operations, for example, n² and n⁴ are not that different.
- **Constant**: O(1). Printing a text in console.
- **Logarithmic**: 0(log n). [[binary-search|Binary search]].
- **Linear**: 0(n). Looping trough an array from beginning to the end.
- **Quasilinear or linearithmic**: O(n log n). [[merge-sort|Merge sort]].
- **Quadratic or polynomial**: O(n²). [[bubble-sort|Bubble sort]].
- **Exponential**: O(2^n). Guessing a password with a brute-force approach.
- **Factorial**:  0(n!). Getting all permutations of an array.