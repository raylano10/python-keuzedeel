import random


def roll():
    min_value = 1

    max_value = 6

    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Voer het aantal spelers in (2 - 4): ")


    if players.isdigit():  
        players = int(players)


        if 2 <= players <= 4: #zorgt ervoor dat er maar minimaal 2 spelers spelen of max 4 speler 
            break


        else:
            print("Het aantal spelers moet tussen 2 en 4 zijn.")

    else:
        print("Incorrect, probeer het opnieuw..")

max_score = 120
player_scores = [0 for _ in range(players)]   # het zet een nul voor elke speler die mee doet

while max(player_scores) < max_score:  # dit zorgt ervoor dat het spel doorgaat tot de spelers op het max score zijn

    for player_idx in range(players):

        print("\nBeurt van speler nummer", player_idx + 1, "is begonnen!")
        print("je totale score is:", player_scores[player_idx], "\n")

        current_score = 0


        while True:
            should_roll = input("Wil je gooien (y)? ")
            if should_roll.lower() != "y":  # de speler moet y klicken om door te spelen om de de dobbel steen te gooien
                break


            value = roll()
            if value == 1:
                print("Je gooide een 1! beurt voorbij!")
                current_score = 0
                break

            else:
                current_score += value
                print("Je gooide:", value)


            print("Je score is:", current_score)


        player_scores[player_idx] += current_score
        print("Je totale score is:", player_scores[player_idx])



max_score = max(player_scores)

winning_idx = player_scores.index(max_score)  #dit zorgt dat de speler die gewonnen heeft heeft als winnaar word aangegeven in de volgende codering

print("Speler nummer", winning_idx + 1,
      "is de winnaar met een score van::", max_score)