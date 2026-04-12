"""
A deep choose‑your‑adventure game with 15 decision points.
The player navigates a mysterious island with a rich story.
"""

# ASCII Art for the game opening
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=. |                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:="=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; ." ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Chronicles of the Forgotten Island.")
print("Your plane crashed. You wake up on a sandy beach. Your mission: Find the treasure and escape.")

# Question 1: Initial Direction
q1 = input("1. You see a dark jungle to the 'Left' and a rocky cliff to the 'Right'. Where do you go? ").title()
if q1 == "Left":
    # Question 2: Jungle Encounter
    q2 = input("2. You hear a rustle. Do you 'Hide' or 'Investigate'? ").title()
    if q2 == "Investigate":
        # Question 3: The Native
        q3 = input("3. It's a friendly native. He offers a 'Map' or 'Food'. Which do you take? ").title()
        if q3 == "Map":
            # Question 4: The River
            q4 = input("4. The map leads to a river. Do you 'Build' a raft or 'Swim'? ").title()
            if q4 == "Build":
                # Question 5: The Waterfall
                q5 = input("5. You're on the raft. A waterfall appears! Do you 'Jump' or 'Stay' on the raft? ").title()
                if q5 == "Jump":
                    # Question 6: The Cave
                    q6 = input("6. You land in a pool by a cave. Enter the 'Cave' or 'Climb' out? ").title()
                    if q6 == "Cave":
                        # Question 7: The Fork
                        q7 = input("7. Inside the cave, it's dark. Go 'Deep' or stay 'Near' the light? ").title()
                        if q7 == "Deep":
                            # Question 8: The Bridge
                            q8 = input("8. You find a rope bridge. Do you 'Cross' it or find another 'Way'? ").title()
                            if q8 == "Cross":
                                # Question 9: The Guardian
                                q9 = input("9. A stone golem guards a door. 'Fight', 'Talk', or 'Run'? ").title()
                                if q9 == "Talk":
                                    # Question 10: The Riddle
                                    q10 = input("10. Golem asks: 'What has keys but no locks?' (Piano/Map/Wind): ").title()
                                    if q10 == "Piano":
                                        # Question 11: The Treasure Room
                                        q11 = input("11. Door opens to three chests: 'Gold', 'Silver', or 'Iron'? ").title()
                                        if q11 == "Iron":
                                            # Question 12: The Escape
                                            q12 = input("12. You found a key in the iron chest! Use it on the 'Hatch' or the 'Gate'? ").title()
                                            if q12 == "Hatch":
                                                # Question 13: The Tunnel
                                                q13 = input("13. A tunnel leads to a 'Boat' or a 'Plane'? ").title()
                                                if q13 == "Boat":
                                                    # Question 14: The Sea
                                                    q14 = input("14. You are at sea. A storm hits! 'Anchor' or 'Full Speed'? ").title()
                                                    if q14 == "Anchor":
                                                        # Question 15: The End
                                                        q15 = input("15. A rescue ship arrives. 'Signal' them or 'Wait'? ").title()
                                                        if q15 == "Signal":
                                                            print("YOU ESCAPED WITH THE TREASURE! YOU WIN!")
                                                        else: print("The ship passed by. You are stranded. Game Over.")
                                                    else: print("The boat capsized. Game Over.")
                                                else: print("The plane has no fuel. Game Over.")
                                            else: print("The gate is a trap. Game Over.")
                                        else: print("The chest was full of snakes! Game Over.")
                                    else: print("Wrong answer. The Golem crushed you. Game Over.")
                                else: print("You can't outrun/outfight a Golem. Game Over.")
                            else: print("You got lost in the darkness. Game Over.")
                        else: print("The tide came in and flooded the entrance. Game Over.")
                    else: print("The climb was too steep. You fell. Game Over.")
                else: print("The raft shattered on the rocks. Game Over.")
            else: print("Piranhas attacked you! Game Over.")
        else: print("The food was poisonous. Game Over.")
    else: print("A panther found your hiding spot. Game Over.")
else:
    print("You fell off the cliff. Game Over.")"
