# Is he gonna survive? (8th Kyu)
# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons!
# Each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.
# Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Solutuion One: Simple
def hero(bullets, dragons):
    if bullets >= dragons * 2:
        return True
    else:
        return False

# Solution Two: Advanced
def hero(bullets, dragons):
    return bullets >= dragons * 2


# Solution Three: Community
# Never even considered lambda, it's basically a mini-function with one output.
hero = lambda d, b: d >= b*2
