#Hangman.py
#By Joshua Yuill

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.




###########################################################################################
#   ____  ____  _______   __   _____   __   ________________  __  ________   _____    __  #
#  / __ \/ __ \/ ____/ | / /  /  _/ | / /  /_  __/ ____/ __ \/  |/  /  _/ | / /   |  / /  #
# / / / / /_/ / __/ /  |/ /   / //  |/ /    / / / __/ / /_/ / /|_/ // //  |/ / /| | / /   #
#/ /_/ / ____/ /___/ /|  /  _/ // /|  /    / / / /___/ _, _/ /  / // // /|  / ___ |/ /___ #
#\____/_/   /_____/_/ |_/  /___/_/ |_/    /_/ /_____/_/ |_/_/  /_/___/_/ |_/_/  |_/_____/ #
###########################################################################################







# VVVVV The Code Is Down Here VVVVVV

############################################################################################################################################################################################################################################



import random

def Logo():
    print(" _    _                                                    __                ")
    print("| |  | |                                                  (  )               ")
    print("| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __             ||                ")
    print("|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \            ||                ")
    print("| |  | | (_| | | | | (_| | | | | | | (_| | | | |       ___|^^|__.._          ")
    print("|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|      /____________\         ")
    print("                     __/ |                            \____________/~~~.     ")
    print("                    |___/                                                    ")
    print("                                                                             ")
    Main_Menu()
    return

def Main_Menu():
    Answer = False
    print("WELCOME! To Hangman, Please Select An Option")
    print(" ")
    print("1 - Play Game")
    print("2 - Quit")

    chosen = input("Please Type your Option Number: ")

    if chosen == "1":
        print("                    ")
        Main()
    elif chosen == "2":
        r_u_sure = input("Are you Sure You Want To Quit? [Y/N]: ")

        if r_u_sure == "Y" or r_u_sure == "y":
                quit
                
        elif r_u_sure == "N" or r_u_sure == "n":
            print("                                                             ")
            print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print("V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V")
            print("                                                             ")
            Main_Menu()
        else:
            exit
                
    else:    
        print("--> That Was An Incorect Input , Please Try Again <--")
        print(" ")
        Main_Menu()

        return


def Clear():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    Logo()
    return
    
    































def Main():
    print(" ")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    Length = 0
    Count = 0

    WORD = (random.choice(open("Words.txt").read().split()))

    Letter = list(WORD)

    for i in Letter:
        Length = Length + 1

    Blanks = ["_"] * Length


    print(Blanks)
    print(" ")
    Guess_Count = 12


    for i in range(1,100):
        guess = input("Please Guess A Letter: ")
        Count = 0
        Wrong = True
        Correct = False
        for i in Letter:
            if guess == Letter[Count]:
                Wrong = False
                Correct = True
                Blanks[Count] = Letter[Count] 
                            
            Count = Count + 1

        if Wrong == True:
            Guess_Count = Guess_Count - 1
            print("------------------------------------------------------")
            print(" ")
            print("That Answer Was Inncorrect, Guesses Left = ", Guess_Count)
            print(" ")
            print(Blanks)
            print(" ")
    
        
        
        elif Correct == True:
            print("------------------------------------------------------")
            print(" ")
            print("That Answer Was Correct!, Guesses Left = ", Guess_Count)
            print(" ")
            print(Blanks)
            print(" ")
        
        if Letter == Blanks:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("/$$     /$$ /$$$$$$  /$$   /$$       /$$      /$$ /$$$$$$ /$$   /$$")
            print("|  $$   /$$//$$__  $$| $$  | $$      | $$  /$ | $$|_  $$_/| $$$ | $$")
            print(" \  $$ /$$/| $$  \ $$| $$  | $$      | $$ /$$$| $$  | $$  | $$$$| $$")
            print("  \  $$$$/ | $$  | $$| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$")
            print("   \  $$/  | $$  | $$| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$")
            print("    | $$   | $$  | $$| $$  | $$      | $$$/ \  $$$  | $$  | $$\  $$$")
            print("    | $$   |  $$$$$$/|  $$$$$$/      | $$/   \  $$ /$$$$$$| $$ \  $$")
            print("    |__/    \______/  \______/       |__/     \__/|______/|__/  \__/")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("YOU WIN!! YOU HAD", Guess_Count ,"GUESSES LEFT")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            again = input("Play Again? [Y/N]: ")
                 
            if again == "Y" or again == "y":
                Clear()
            else:
                quit
                break

        if Guess_Count == 0:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗")
            print(" ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝")
            print("  ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ")
            print("    ██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ")
            print("    ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗")
            print("    ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("YOU LOSE!! BETTER LUCK NEXTIME")
            print(" ")
            print(" ")
            print("THE ANSWER WAS *",WORD)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            again = input("Play Again? [Y/N]: ")
                 
            if again == "Y" or again == "y":
                Clear()
            else:
                quit
                break
        


    
        














Logo()
