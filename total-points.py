# Total amount of points (8th Kyu)
# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

points = (['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])

# Solutuion One: Simple
def points(games):
    score = 0
    for game in games:
        x, y = map(int, game.split(":"))
        if x > y:
            score += 3
        elif x == y:
            score += 1
    return score

# Solution Two: Advanced
# Used the map() function with str.partition to split each match result into three parts
def points(games):
    return sum(3 if x > y else 1 if x == y else 0 for x, y in (result.split(':') for result in games))

# Solution Three: Community
# Same same the simple solution, but simpler.
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count
