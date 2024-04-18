# Thinkful - Logic Drills: Traffic light (8th Kyu)
# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

# Solution 1: Simple
def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'

# Solution 2: Advanced
# Add a dictionary, return the [current] entry in the dictionary.
def update_light(current):
    return {'green': 'yellow', 'yellow': 'red', 'red': 'green'}[current]
#   return {"green": "yellow", "yellow": "red", "red": "green"}.get(current, "Invalid")

# Solution 3: Community
# Noting special, but does contain an error state, which is nice.
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."
    
