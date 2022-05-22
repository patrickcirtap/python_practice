"""

Given an array of integers (ints) sorted in ascending order,
find the starting and ending position of a given value (target).
Return the start and end positions of target in a tuple.
If target is not in the array, return (-1, -1)


Example 1:
    Input:  [5, 7, 7, 7, 8, 8, 11], 7
    Output: (1, 3)
    Explanation: The first occurence of 7 is at position 1 and
                 the final occurence of 7 is at position 3.

Example 2:
    Input:  [5, 7, 7, 8, 8, 10], 6
    Output: (-1, -1)

Constraints:
    - ints is sorted in ascending order
    - ints.length >= 0

"""

def element_range_in_sorted_array(ints, target):
    # Your code goes here
