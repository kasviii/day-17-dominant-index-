Dominant Index Finder
This Python script finds the dominant index in a given list of integers.

Overview
Given a list of integers, the dominant index is defined as the index of the largest integer such that for every other number in the array x, the largest integer is at least twice as big as x.

For example:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer in the list. For every other number in the array x, 6 is at least twice as big as x. The index of the value 6 is 1, so the function returns 1.
Usage
You can use the dominant_index function provided in the dominant_index.py file to find the dominant index in a given list of integers.

How It Works
The dominant_index function first finds the maximum number in the list and its index. Then, it iterates through the list again to check if for every number num, the maximum number is at least twice as big as num. If this condition fails for any number, the function returns -1. Otherwise, it returns the index of the maximum number.
