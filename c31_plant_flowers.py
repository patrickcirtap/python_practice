"""

You have a long flowerbed in which some of the pots are planted,
and some are not. However, flowers cannot be planted in adjacent plots.

Given:
    - an integer array (flowerbed) containing 0's and 1's,
      where 0 means empty and 1 means not empty, and
    - an integer n,
return if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule.

Note that there will always be a flower potted at the
beginning of the flowerbed and at the end of the flowerbed.

Example 1:
    Input:  [1, 0, 0, 0, 1], 1
    Output: true
    Explanation: 1 flower needs to be potted and there is a
                 position in the flowerbed that can have a flower
                 without violating the no-adjacent-flowers rule

Example 2:
    Input:  [1, 0, 0, 0, 1], 2
    Output: false

Example 3:
    Input:  [1, 0, 0, 1], 1
    Output: false

Example 4:
    Input: [1, 0, 0, 0, 0, 0, 0, 1], 2
    Output: true
    Explanation: The flowerbed could be one of the following:
                     [1, 0, 1, 0, 1, 0, 0, 1] or
                            ^     ^
                     [1, 0, 0, 1, 0, 1, 0, 1]
                               ^     ^

Constraints:
    - flowerbed.length >= 1
    - flowerbed[i] is 0 or 1
    - the first and last element of flowerbed is 1
    - there are no two adjacent flowers in flowerbed
    - n >= 0

"""

def plant_flowers(flowerbed, n):
    # Your code goes here
