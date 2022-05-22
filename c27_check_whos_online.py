"""

Given a list of dicts (friends), representing a list of friends online,
return a sorted list of all the friends who are currently online.
If no one is online, return -1.


Example 1:
    Input:  [
              {
                "name": "Steve",
                "status": "online"
              },
              {
                "name": "Alice",
                "status": "offline"
              },
              {
                "name": "Bob",
                "status": "online"
              }
            ]
    Output: ["Bob", "Steve"]

Example 2:
    Input:  [
              {
                "name": "Staramama",
                "status": "offline"
              }
              {
                "name": "Nono",
                "status": "offline"
              }
            ]
    Output: -1

"""

def check_whos_online(friends):
    # Your code goes here
