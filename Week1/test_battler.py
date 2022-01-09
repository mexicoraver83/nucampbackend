# Task 1 - Declaring game character variables

wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

# Declaring HP for each character

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 200

# Declaring damage for each character

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 200

# Declaring dragon HP and Damage

dragon_hp = 300
dragon_damage = 50

game_on = True
# Task 3 - Create the Infinite Loop
while game_on == True:

    while True:

        # Task 2 - Prompt the player to choose from a list of options.

        print("1)    ", wizard)
        print("2)    ", elf)
        print("3)    ", human)
        print("4)    ", orc)
        print("5)     Exit")

        # Player selects character using input option.  Used int to change input from string to integer
        # Bonus Task 1 - Allow player to select with number OR name (turn numbers into strings)
        # Bonus Task 2 - Allow any case (use .lower())

        player_choice = input("Choose your character: ").lower()

        # if statements to determine player_choice
        if (player_choice == "1") or (player_choice == "wizard"):
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print("You have chosen ", wizard)
            print("Health: ", wizard_hp)
            print("Damage: ", wizard_damage)
            break
        if (player_choice == "2") or (player_choice == "elf"):
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print("You have chosen ", elf)
            print("Health: ", elf_hp)
            print("Damage: ", elf_damage)
            break
        if (player_choice == "3") or (player_choice == "human"):
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print("You have chosen ", human)
            print("Health: ", human_hp)
            print("Damage: ", human_damage)
            break
        if (player_choice == "4") or (player_choice == "orc"):
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            print("You have chosen ", orc)
            print("Health: ", orc_hp)
            print("Damage: ", orc_damage)
            break
        if (player_choice == "5") or (player_choice == "exit"):
            print("Game Exited")
            quit()
        else:
            print("Unknown Character")

            # Task 4 - Battle wih the Dragon, remember to set the variable to x = x-y

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon_hp)
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at", character)
        print("The", character, "hitpoints are now:", my_hp)
        if my_hp <= 0:
            print("The", character, "has lost the battle.")
            break
        game_on = False
    choice = input("Would you like to play again? Y or N: ").lower()
    if choice == "y":
        game_on = True
    else:
        game_on = False
