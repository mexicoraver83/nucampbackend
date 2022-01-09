# Declaring characters
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
exit = "Exit"

game_start = True
while game_start == True:

    # Assigning hitpoints to the characters
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 200

    # Assigning damage to the characters
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 30

    # Assigning hitpoint and damage to the dragon
    dragon_hp = 300
    dragon_damage = 50

    # Showing characer options
    while True:
        print("1)   Wizard")
        print("2)   Elf")
        print("3)   Human")
        print("4)   Orc")
        print("5)   Exit")
        character = input("Choose your character: ")
        # print(character)
        if character == "1" or character.casefold() == "Wizard".casefold():
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print("You have chosen the character: ", character)
            print("Health: ", my_hp)
            print("Damage: ", my_damage, "\n")
            break
        elif character == "2" or character.casefold() == "Elf".casefold():
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print("You have chosen the character: ", character)
            print("Health: ", my_hp)
            print("Damage: ", my_damage, "\n")
            break
        elif character == "3" or character.casefold() == "Human".casefold():
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print("You have chosen the character: ", character)
            print("Health: ", my_hp)
            print("Damage: ", my_damage, "\n")
            break
        elif character == "4" or character.casefold() == "Orc".casefold():
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            print("You have chosen the character: ", character)
            print("Health: ", my_hp)
            print("Damage: ", my_damage, "\n")
            break
        elif character == "5" or character.casefold() == "Exit".casefold():
            print("Goodbye")
            quit()
            # raise SystemExit
        else:
            print("Unknown character")
    # Initiating the battle
    # First character attack
    while True:
        # print("Original health of Dragon is: ", dragon_hp)
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoint are now: ", dragon_hp, "\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        # Dragon attacks back
        else:
            # print("My original health is: ", my_hp)
            my_hp = my_hp - dragon_damage
            print("The Dragon strikes back at ", character)
            print("The", character, "'s hitpoints are now: ", my_hp, "\n")
            if my_hp <= 0:
                print("The", character, "has lost the battle", "\n")
                break
    game_start = False

    continue_playing = input("Want to play again: Y or N: ")
    if continue_playing.casefold() == "Y".casefold():
        game_start = True
    else:
        game_start = False
