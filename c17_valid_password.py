"""

Given a string representing a password, return true if
it meets the following password constraints:
    1. Is at least ten (10) characters long
    2. Contains at least one uppercase letter
    3. Contains at least one lowercase letter
    4. Contains at least one digit:
    5. Contains at least one special character:
        ! @ # $ % ^ & *
    6. Contains at least one bracket:
        ( ) [ ] { } < >

Return false otherwise.


Example 1:
    Input:  "p@s$W0rd>>"
    Output: true
    Explanation: The password is 10 characters long and
                 contains all necessary character types

Example 2:
    Input:  "p@s$W0rd>"
    Output: false
    Explanation: The password is not 10 characters long

Example 3:
    Input:  ""
    Output: false

Example 4:
    Input:  "zX<%5kL{}12#"
    Output: true

"""


def valid_password(password):
    # Your code goes here
