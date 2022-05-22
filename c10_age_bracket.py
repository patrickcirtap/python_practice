"""

Given someone's age in years, return what age bracket they are in.
Age brackets are labelled such that:
    - The lower bound is inclusive
    - The upper bound is exclusive

0 years   - 18 months: infant
18 months - 3 years:   toddler
3 years   - 5.5 years: young child
5.5 years - 10 years:  child
10 years  - 13 years:  adolescent
13 years  - 19 years:  teenager
19 years  - 21 years:  young adult
21 years  - 30 years:  the prime of your life
30 years  - 52 years:  old, eww
52 years  - 60 years:  mid-life, lol
60 years  - 80 years:  damn still going...
80 years  - 95 years:  how are you still alive?
95 years  - 103 years: this is getting out of hand
103 years +            the wind could kill you


Example 1:
    Input:  3
    Output: young child

Example 2:
    Input:  1.25
    Output: infant

Example 3:
    Input:  54
    Output: mid-life, lol

Constraints:
    age >= 0

"""

def age_bracket(age):
    # Your code goes here
