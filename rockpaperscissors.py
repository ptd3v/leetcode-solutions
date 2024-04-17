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