# Python Loop Performance

This experiment is designed to compare the performance of `for` and `while` loops in Python. Specifically, we will create two functions that calculate the sum of all numbers from 1 to n, one using a `for` loop and the other using a `while` loop. We will then measure the execution time of each function for different values of n and compare their performance.

## Objective

The objective of this experiment is to determine which of the two loops performs better in terms of execution time for calculating the sum of all numbers from 1 to n.

## Methodology

1.  Create a function that calculates the sum of all numbers from 1 to n using a `for` loop.
2.  Create a function that calculates the sum of all numbers from 1 to n using a `while` loop.
3.  Import the `time` module to measure the execution time of each function.
4.  Call the functions using different values of n (10, 100, 1,000, 10,000, 100,000).
5.  Record the execution time for each function.
6.  Compare the execution times of the `for` and `while` loops for each value of n.

## Conclusion

Based on the results of the experiment, the `for` loop performs better than the `while` loop in terms of execution time for calculating the sum of all numbers from 1 to n. For small values of n, the execution time for both loops is almost the same, but as n increases, the difference in execution time becomes more pronounced.