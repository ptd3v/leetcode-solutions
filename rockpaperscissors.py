# Functional Rock Paper Scissors
def rockpaperscissors():
    player1 = input("Player 1, choose rock, paper, or scissors: ").lower()
    player2 = input("Player 2, choose rock, paper, or scissors: ").lower()

    if player1 == player2:
        return "Draw"
    if (player1 == "rock" and player2 == "scissors") or \
       (player1 == "scissors" and player2 == "paper") or \
       (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

result = rockpaperscissors()
print("Result:", result)

# Rock Paper Scissors - CodeWars (8th Kyu)
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Solution:
# Summary: There are only three possible win/ loss conditions. All else results in Player2 winning.
def rockpaperscissors(player1, player2):
    if player1 == player2:
        return "Draw"
    if (player1 == "rock" and player2 == "scissors") or \
       (player1 == "scissors" and player2 == "paper") or \
       (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

# Community Solution:
# Summary: Use a dictionary called 'beats'. Wow, I love this.
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'} # Define a dictionary representing the winning relationships between choices
    if beats[p1] == p2: # Check if player 1's choice beats player 2's choice
        return "Player 1 won!"
    if beats[p2] == p1: # Check if player 2's choice beats player 1's choice
        return "Player 2 won!"
    return "Draw!" # If neither player wins based on the dictionary 'beats', return "Draw!"
