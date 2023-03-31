from sqlalchemy import *
from sqlalchemy.orm import *
import colorama
from playsound import playsound
from tables import Result
from training_ground import training_ground

def quest_witch(session, knight_full_title, knight_short_title, current_knight_id):
    print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT +

        '''
   '.  `~~`~`~~^`~~`~^~^`~~`~~`~^~`.   .`     /
     `> ' . ' ". _ '-"`  .  ` ' .   | .    ' /
    .' ,'~^~^~^`^~~^`^~`~~~^~~~^;       ' ' |
    .-'                          \ ` : ` . "|
                                /| : |  . | |
                               / |    '   " |
                         __.--~\ |  |   : . |
                        `~--.__/ | .  '     |
                              \  | .' |  ' "|
                               \_|  .    _ .|   _.-")
                               / \______//  |.-"_.-"
                              / \___/_ \ | .|.-"
                             /   |   /\/ /" |
                            /    | ./   /   |
                         _.(     |_ \__/ ' '|
               __    _.-"_.-\   /_ \:   | . |
          _.=~\ _\.-"_.-'    )  \ \=\  .'   |
      _.=~_.=~ \.-\-"       /    | \=\__  | |
       .=~_.=~_ \_/         \   (   \___\  '|
        =~_.=~_.=`           \___)  |  .    |
         ~_.=~                   | '   "   '|
                                 | . " | ' .|
  '-"_'"-'_"'-_'"-_''_"-"-_"-\ \/'   '   . '`\/"/- '"-_-"'_
 -_ --"-"_ _ _""-_'"--"'_-"-' \/. _' / /".\,//\//'-"-_'"-"'_
    -"-'_-"_-"-_"-"'_'-"-"_``"-`"_`'""-`''""'-_'"-"-_"'"-
        '''
    )
    print("The Witch Trial of Camelot")
    print(colorama.Style.RESET_ALL)
    input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
    print(colorama.Style.RESET_ALL)
    print(f"A woman in Sir Bedivere's town is accused of being a witch. It is up to you, {knight_short_title} to decide if she is or is not a satanist witch.\nWhat do you know about witches that can help you solve this mystery?")
    in_program = True
    while in_program:
        witch_1_input = input(colorama.Fore.YELLOW + colorama.Style.BRIGHT +"     A) If she is made of wood, she is a witch \n     B) If she is wearing a pointed hat, she is a witch. \n(A / B) ").lower()
        print(colorama.Style.RESET_ALL)
        if witch_1_input == "a": 
            # correct
            print("Of course all witches are made of wood! Even a peasent would know that. \nBut how should you check if she is made of wood without killing a potentially innocent person?")
            playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/sound-effect-twinklesparkle-115095.mp3')
            witch_2_input = input(colorama.Fore.YELLOW + colorama.Style.BRIGHT +"     A) Burn her!!!! \n     B) Check if she floats. \n(A / B) ").lower()
            print(colorama.Style.RESET_ALL)
            if witch_2_input == "a":
                print(f"\n{knight_full_title} - clearly you are not an honorable knight. You would have us burn a person before we have found them guilty of being a witch? \n You are banished from the town for your poor decision making.")
                input(colorama.Fore.CYAN + "\n   Click enter/return to continue \n")
                playsound("/Users/abbysmith/Development/code/phase-3/phase3_quest/failure-drum-sound-effect-2-7184.mp3")
                print(colorama.Style.RESET_ALL)
                # Failure
                new_result = Result(
                    knight_id = current_knight_id,
                    quest_id = 1,
                    outcome = "loss"
                    )
                session.add(new_result)
                session.commit()
                in_program = False
                training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                
                # Send to training ground
            elif witch_2_input == "b":
                # correct
                print(f"{knight_full_title}, you are clearly a person who has an expansive scientific knowledge! \nThe nearest body of water is much too far away to drag this woman. How else could we check if she floats?")
                playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/sound-effect-twinklesparkle-115095.mp3')
                witch_3_input = input(colorama.Fore.YELLOW + colorama.Style.BRIGHT +"     A) See if she can turn David into a newt \n     B) Check if she weighs the same as a duck \n(A / B) ").lower()
                print(colorama.Style.RESET_ALL)
                if witch_3_input == "a":
                    print(f"\n{knight_full_title} - I am ashamed of you. You would risk the life of the knowledgable David by sacrificing him to potintally become a newt?!? \nAn angry mob runs you out of the village.")
                    playsound("/Users/abbysmith/Development/code/phase-3/phase3_quest/failure-drum-sound-effect-2-7184.mp3")
                    input(colorama.Fore.CYAN + "\n   Click enter/return to continue \n")
                    print(colorama.Style.RESET_ALL)# Failure
                    new_result = Result(
                        knight_id = current_knight_id,
                        quest_id = 1,
                        outcome = "loss"
                        )
                    session.add(new_result)
                    session.commit()
                    in_program = False
                    training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                    # Send to training ground
                elif witch_3_input == "b":
                    playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/sound-effect-twinklesparkle-115095.mp3')
                    print("\nYES! A duck floats, thus anything that weighs more than a duck would not float.\nThis is irrefutable logic. \n")
                    input(colorama.Fore.CYAN + "\n   Click enter/return to continue \n")
                    print(colorama.Style.RESET_ALL)
                    print("The townspeople take the woman to the scales and compares her weight to a duck. \nShe weighs more than the duck! She is a witch! \nYou have saved the town from the evils of the occult and they will build a statue in honor of you (after they burn the witch, of course).") 
                    input(colorama.Fore.CYAN + "\n   Click enter/return to continue \n")
                    print(colorama.Style.RESET_ALL)
                    print("Return to the training ground.")
                    # SUCCESSFUL QUEST
                    new_result = Result(
                        knight_id = current_knight_id,
                        quest_id = 1,
                        outcome = "win"
                        )
                    session.add(new_result)
                    session.commit()
                    in_program = False
                    training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                else:
                    print("Answer the question! Select A or B\n") 
                    witch_3_input
            else:
                print("Answer the question! Select A or B\n")
                witch_2_input
                # Continue
        elif witch_1_input == "b":
            print("\nYou fool. Any townsperson could have put the pointed hat on their head. \nMaybe you are the witch. \nWe'll need to burn you at the stake just to be sure.\n")
            playsound("/Users/abbysmith/Development/code/phase-3/phase3_quest/failure-drum-sound-effect-2-7184.mp3")
            input(colorama.Fore.CYAN + "\n   Click enter/return to continue \n")
            print(colorama.Style.RESET_ALL)
            print("You flee the scene in disgrace")
            input(colorama.Fore.CYAN + "\n   Click enter/return to continue \n")
            print(colorama.Style.RESET_ALL)
            #Failure
            new_result = Result(
                knight_id = current_knight_id,
                quest_id = 1,
                outcome = "loss"
                )
            session.add(new_result)
            session.commit()
            in_program = False
            training_ground(session, knight_full_title, knight_short_title, current_knight_id)

        else:
            print("Answer the question! Select A or B\n")
            witch_1_input

