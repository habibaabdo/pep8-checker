# IMPPRTING modules.
import time
import random


def play_game():
    # YOUR game code goes here.
    def print_pause(print_pause):
        # FUNCTION for printing after 2 secs.
        print(print_pause)
        time.sleep(2)
    print_pause(print_pause)

    # to check weather the user enterd avalid input or no
    def val_input():
        input_value = input("(what's your choice?)please enter 1 or 2: ")
        if input_value not in ["1", "2"]:
            val_input()
        return input_value

    print_pause("are you ready to play ?")
    print_pause("are you brave enough to play this game?!")
    print_pause("let's get started!")
    name = input("please enter your name to continue: ")
    print_pause("welcome to you " + name)

    # describing what is happining(intro)
    def introduction():
        options = [
            "now you found yourself thrown on the floor",
            "you wake up on the ground, disoriented",
            "as you come to, you realize that you're lying on the floor",
            "you slowly open your eyes and take in your surroundings",
            "you find yourself in a strange place, lying on the ground"]
        print_pause(random.choice(options))

        options = [
            "You can't seem to remember anything \
            \nabout what happened that night",
            "Your mind is blank, and you can't recall anything that happened",
            "Your memory is hazy, and you can't remember how you got here",
            "You're struggling to piece together what happened,\
                \n but your mind is foggy",
            "You're completely lost,\
            \n with no recollection of how you ended up here"]
        print_pause(random.choice(options))

        options = [
            "You can't remember how you ended up in this strange village",
            "This village is completely unfamiliar to you",
            "You have no idea how you got here",
            "The last thing you remember is fighting a wicked witch",
            "Your mind is a blur, \
            \n but you recall a fierce battle with a wicked witch"]
        print_pause(random.choice(options))

        options = [
            "You're not sure if the witch \
            \n managed to kidnap your sister or not",
            "You can't recall if the witch was able to take your sister",
            "You have no idea if your sister was taken by the witch",
            "Your memory is fuzzy, but you think the witch \
                \n might have taken your sister"]
        print_pause(random.choice(options))

        options = [
            "Perhaps she succeeded while you were lying on the ground",
            "Maybe she managed to take your sister while you were unconscious",
            "It's possible that she took \
            \n your sister while you were incapacitated",
            "You're not sure if she took your sister \
                \n before or after casting the spell",
            "The spell she cast on you must\
            \n have been powerful to wipe your memory"]
        print_pause(random.choice(options))

        options = [
            "You suddenly realize that you don't even know where you are",
            "You've been so preoccupied \
            \n that you've lost track of your location",
            "You curse the wicked witch for putting you in this situation",
            "You're not sure if this village is the witch's home or not",
            "You must find your sister \
            \n and get out of here as soon as possible"]
        print_pause(random.choice(options))

        options = [
            "Now you must decide whether to rescue your sister or run away",
            "It's up to you to save your sister\
            \n or flee from the witch's clutches",
            "You have a choice to make: \
            \n save your sister or escape from the village",
            "Your sister's fate is in your hands, \
            \n will you rescue her or abandon her?",
            "You must act quickly - will you be a hero or a coward?"]
        print_pause(random.choice(options))

    introduction()

    # ask the player to choose whether to save their sister or run away
    print_pause("choose 1 to save your sister ")
    print_pause("choose 2 to run away")

    def saving_sister():
        score = 0
        choice = val_input()

        if choice == "1" :
            # add 10 points for choosing to save sister
            score += 10
            print_pause("Congratulations! You have earned 10 points!")
            # concatenate score to the string and print it
            print_pause("Your current score is: " + str(score))
            print_pause("You stand up from the place you were thrown and look around.")
            print_pause("You see the huge and ominous palace looming in the distance.")
            print_pause("The path leading to it is overgrown and treacherous.")
            print_pause("Enter 1 to cautiously enter the forest\
                \n and make your way to the palace.")
            print_pause("Enter 2 to try to follow the path and make your way to the palace.")
            # ask the player to choose whether to enter the forest or follow the path
            choice = val_input()

            # update score based on player's choice
            if choice == "1" :
                print_pause("You cautiously enter the forest and make your way to a clearing.")
                print_pause("In the center of the clearing is a strange statue, \
                    \n with a plaque that reads'Only the pure of heart may pass.'")
                print_pause("Enter 1 to touch the statue.")
                print_pause("Enter 2 to leave the clearing and continue through the forest.")
                choice = val_input()

                if choice == "1" :
                    print_pause("You feel a jolt of electricity run through your body, \
                        \n but you also feel a newfound sense of strength and purity.")
                    print_pause("The path to the palace is now clear and you make your way towards it.")
                    # add 10 points for touching the statue
                    score += 10
                else:
                    print_pause("You decide to leave the clearing \
                        \n and continue through the forest.")
            else:
                print_pause("You try to follow the path, \
                    \n but it quickly becomes too overgrown and treacherous.")
                print_pause("You are forced to turn back \
                    \n and look for another way to the palace.")

            # ask the player to choose whether to enter the palace carefully or stealthily
            if score > 0 :
                print_pause("You arrive at the palace gates, guarded by two fierce warriors.")
                print_pause("Enter 1 to approach the guards carefully and try to talk your way in.")
                print_pause("Enter 2 to try to sneak past the guards \
                    \n and enter the palace undetected.")
                choice = val_input()

                # update score based on player's choice
                if choice == "1" :
                    print_pause("You approach the guards carefully, \
                        \n using your wit and charm to convince them to let you in.")
                    print_pause("You enter the palace and begin your search for your sister.")
                    # add 20 points for entering the palace carefully
                    score += 20
                else:
                    print_pause("You try to sneak past the guards, \
                        \n but they catch you and throw you in the dungeon.")
                    print_pause("You must find a way to escape \
                        \n and continue your search for your sister.")
            else:
                print_pause("You are lost in the forest and unable to continue your journey.")

            # add the new scenario for trying to escape the dungeon with a low score
            if score >= 30 :
                print_pause("You find yourself in a dimly lit cell, \
                    \n with your sister nowhere in sight.")
                print_pause("Enter 1 to try to break down the door and escape.")
                print_pause("Enter 2 to try to confront the witch \
                    \n and force her to reveal the location of your sister.")
                choice = val_input()

                # update score based on player's choice
                if choice == "1" :
                    print_pause("You use all your strength to break down the door,\
                        \n and find your sister cowering in the corner.")
                    print_pause("You lead her to safety and make your escape from the palace.")
                    # add 30 points for escaping the dungeon
                    score += 30
                else:
                    print_pause("You make your way to the throne room,\
                        \n where the witch is waiting for you.")
                    print_pause("She is a formidable opponent, \
                        \n but you use all your skills and \
                        \n knowledge to defeat her and free the land from her tyranny.")
                    # add 50 points for defeating the witch
                    score += 50
            elif score > 0 :
                print_pause("You find yourself in a dimly lit cell,\
                    \n with your sister nowhere in sight.")
                print_pause("Enter 1 to try to break down the door and escape.")
                print_pause("Enter 2 to wait and hope thatsomeone will come to your rescue.")
                choice = val_input()

                # update score based on player's choice
                if choice == "1" :
                    print_pause("You try to break down the door, but it is too strong.")
                    print_pause("You are trapped in the dungeon, with no hope of escape.")
                else:
                    print_pause("You wait in the cell,\
                        \n hoping that someone will come to your rescue.")
                    print_pause("But no one comes, and you remain trapped in the dungeon.")

            #check the player's final score and determine whether they have won or lost
            def win_lose():
                if score >= 50:
                    # If 'score' is greater than or equal to 50, print a message indicating that the player has won
                    print_pause("congratulations you win the game!")
                    print_pause("Congratulations! You have defeated the witch and saved the land!")
                    # Print the final score
                    print_pause("Your final score is " + str(score) + ".")
                else:
                    print_pause("Sorry, you have lost the game.")
                    print_pause("Your final score is " + str(score) + ".")
                    print_pause("Better luck next time!")
            win_lose()

        else:
            def run_away() :
                score = 0
                options = ["Sorry, you chose to run away. You don't earn any points", 
                    "You decide to flee from the witch. No points for you.", 
                    "Running away from the witch won't earn you any points.", 
                    "You turn tail and run, but you don't earn any points for it.", 
                    "You run for your life, but your cowardice costs you points."]
                print_pause(random.choice(options))
                # concatenate score to the string and print it
                print_pause("Your current score is: " + str(score)) 
                # ask the player to choose whether to fight or run
                print_pause("You stand your ground, \
                    \n facing the wicked witch as she chants her spells.")
                print_pause("Enter 1 to fight the witch with all your might.")
                print_pause("Enter 2 to run away and try to find a place to hide.")
                choice = val_input()

                # update score based on player's choice
                if choice == "1" :
                    print_pause("You gather all your courage and strength,\
                        \n and charge towards the witch.")
                    print_pause("you earned 50 points! congrats!")
                    score += 50
                    print_pause("your score now is " + str(score))
                    print_pause("You fight valiantly, but the witch is too powerful for you.")
                    print_pause("She unleashes a final spell, and everything goes dark.")
                    # subtract 40 points for losing the fight 
                    score -= 40 
                    print_pause("sorry, you lose the game!")
                    print_pause("game over!")
                    print_pause("your final score is " + str(score))

                else:
                    print_pause("You turn and run as fast as you can, \
                        \n trying to put as much distance between you and the witch as possible.")
                    print_pause("You hear her cackling behind you, but you keep going.")
                    print_pause("You eventually find a cave and hide inside, \
                        \n catching your breath and trying to come up with a plan.")
                    # add 10 points for escaping the witch
                    score += 10
                    # ask the player to choose whether to stay in the cave or continue on
                    print_pause("Enter 1 to stay in the cave and wait for the witch to give up.")
                    print_pause("Enter 2 to continue on \
                        \n and try to find a way to defeat the witch.")
                    choice = val_input()

                    # update score based on player's choice
                    if choice == "1" :
                        print_pause("You decide to stay in the cave, \
                            \n hoping that the witch will give up and leave you alone.")
                        print_pause("After a few hours, you hear the witch's voice outside the cave,\
                            \n calling your name.")
                        print_pause(name + " where you are?? get out from your hideout,\
                            \n l'll find you  she said")
                        print_pause("You stay quiet and still, hoping that she will go away.")
                        print_pause("Eventually, the witch leaves,\
                            \n and you are able to leave the cave and continue on your journey.")
                    else:
                        print_pause("You decide to continue on, determined to find a way \
                            \n to defeat the witch and free the land from her tyranny.")
                        print_pause("You explore the area around the cave, \
                            \n looking for any clues or weapons that might help you in your quest.")

                        options = [
                            "After hours of searching, you finally stumble upon an ancient book of spells.", 
                            "As you search the cave, you come across a hidden compartment in the wall.", 
                            "You notice something glinting in the darkness and investigate further,\
                                \n finding an old book of spells.", 
                            "You almost miss it, but your keen eye spots a book hidden among the rocks.\
                                \n It turns out to be an ancient tome of spells."]
                        print_pause(random.choice(options))

                        print_pause("You spend hours studying the book,\
                            \n learning powerful spells and incantations.")

                        options = [
                            "Feeling confident and empowered, you continue on your journey,\
                                \n ready to face the witch once again!", 
                            "With your newfound knowledge, \
                                \n you feel ready to take on the wicked witch and free the land from her grasp!", 
                            "You feel a surge of power as you master the spells in the ancient book. \
                                \n You're ready to take on the witch and win!", 
                            "Your determination is renewed as you learn the secrets of the ancient book.\
                                \n You're ready to face the witch and emerge victorious!"]
                        print_pause(random.choice(options))
                        print_pause("congrats!, you win the game")
                        # print the final score
                        print_pause("Your final score is: " + str(score))
            run_away()
    saving_sister()

def play_again() :
    while True :
        choice = input("Do you want to play again? (y/n)").lower()

        if choice == "y" :
            return True
        elif choice == "n" :
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Main game loop
while True:
    play_game()
    if not play_again():
        break

