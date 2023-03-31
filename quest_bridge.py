from sqlalchemy import *
from sqlalchemy.orm import *
import colorama
import threading
from playsound import playsound
from tables import Result
from training_ground import training_ground

def play_scary():
    playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/dun-dun-duuun-v01-105105.mp3')

def quest_bridge(session, knight_full_title, knight_short_title, current_knight_id):
    print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT +
        '''
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\.
       ::::::;       ;          OOOOO\.
       ;:::::;       ;         OOOOOOOO.
      ,;::::::;     ;'         / OOOOOOO.
    ;:::::::::`. ,,,;.        /  / DOOOOOO.
  .';:::::::::::::::::;,     /  /     DOOOO.
 ,::::::;::::::;;;;::::;,   /  /        DOOO.
;`::::::`'::::::;;;::::: ,#/  /          DOOO.
:`:::::::`;::::::;;::: ;::#  /            DOOO.
::`:::::::`;:::::::: ;::::# /              DOO.
`:`:::::::`;:::::: ;::::::#/               DOO.
 :::`:::::::`;; ;:::::::::##                OO.
 ::::`:::::::`;::::::::;:::#                OO.
 `:::::`::::::::::::;'`:;::#                O.
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
   \n
   Welcome to the Bridge of Death
        '''
    )
    print(colorama.Style.RESET_ALL)
    in_program = True
    while in_program:
        input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
        print(colorama.Style.RESET_ALL)
        print("The holy grail has been rumored to be in the Castle of AARGH, \nwhich can only be reach by crossing the \n BRIDGE OF DEATH.")
        sound_thread = threading.Thread(target=play_scary)
        sound_thread.start()
        input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
        print(colorama.Style.RESET_ALL)
        print("The great and powerful enchanter is gaurding the bridge and will only allow you to cross if you and Sir Galahad can answer these question five (no three).")
        input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
        print(colorama.Style.RESET_ALL)
        print("Question 1: What is your name?")
        
        bridge_1_input = input(colorama.Fore.YELLOW + colorama.Style.BRIGHT +f"     A) Sir Galahad the Chaste and {knight_short_title} \n     B) Tim the Enchanter\n(A / B) ").lower()
        print(colorama.Style.RESET_ALL)
        if bridge_1_input == "a":
            playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/group_yay_cheer-101509.mp3')
            print("Correct, but don't be too proud of yourself. Even a 2 year old knows how to do that")
            input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
            print(colorama.Style.RESET_ALL)
            print("Question2: What is your quest?")
            
            bridge_2_input = input(colorama.Fore.YELLOW + colorama.Style.BRIGHT +"     A) To seek the Holy Grail\n     B) Return to the Castle of Anthrax\n(A / B) ")
            print(colorama.Style.RESET_ALL)
            if bridge_2_input == "a":
                playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/group_yay_cheer-101509.mp3')
                print("We have a good little knight on our hands here who listens to the mission!")
                input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
                print(colorama.Style.RESET_ALL)
                print("Question 3: What is your favorite color?")
                bridge_3_input = input(colorama.Fore.YELLOW + colorama.Style.BRIGHT +"     A) Blue\n     B) Yellow\n(A / B ) ")
                print(colorama.Style.RESET_ALL)
                if bridge_3_input == "b":
                    playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/group_yay_cheer-101509.mp3')
                    #Correct -- REMEMBER THE ANSWER IS YELLOW
                    print("You know your name, quest and favorite color?!? Wooza! You are clearly one of the most intelligent knights in this land.\nYou may cross the bridge to continue the quest for the holy grail.")
                    input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
                    print(colorama.Style.RESET_ALL)
                    new_result = Result(
                        knight_id = current_knight_id,
                        quest_id = 2,
                        outcome = "win"
                    )
                    session.add(new_result)
                    session.commit()
                    in_program = False
                    training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                    
                elif bridge_3_input == "a":
                    print("You lie! Tim the Enchantor can see into your soul and knows that your favorite color is, in fact, YELLOW\nTim the Enchantor explodes you off the edge of the cliff\nThankfully you find a path to the training ground\nOn your walk to the training ground you contemplate other lies you have been telling yourself")
                    playsound("/Users/abbysmith/Development/code/phase-3/phase3_quest/failure-drum-sound-effect-2-7184.mp3")
                    input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
                    print(colorama.Style.RESET_ALL)
                    new_result = Result(
                        knight_id = current_knight_id,
                        quest_id = 2,
                        outcome = "loss"
                    )
                    session.add(new_result)
                    session.commit()
                    in_program = False
                    training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                    pass
                else:
                    print("Answer the question! Select A or B\n ")
                    bridge_3_input
            elif bridge_2_input == "b":
                #Incorrect
                print("While everyone knows that Sir Galhad had a warm welcome at the Castle of Anthrax, \ndo not get tempted with the mysteries that lay in the halls of Castle Anthrax.")
                playsound("/Users/abbysmith/Development/code/phase-3/phase3_quest/failure-drum-sound-effect-2-7184.mp3")
                input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
                print(colorama.Style.RESET_ALL)
                new_result = Result(
                    knight_id = current_knight_id,
                    quest_id = 2,
                    outcome = "loss"
                )
                session.add(new_result)
                session.commit()
                in_program = False
                training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                
            else:
                print("Answer the question! Select A or B\n")
                bridge_2_input
        elif bridge_1_input == "b":
            print(f"I don't know mate, seems like King Arthur should have a knight that at least knows their own name.\nThe standards are not even that high to become a knight.\nMostly the qualifications is to just not die")
            playsound("/Users/abbysmith/Development/code/phase-3/phase3_quest/failure-drum-sound-effect-2-7184.mp3")
            input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
            print(colorama.Style.RESET_ALL)
            print("Tim the Enchantor explodes you off the cliff edge into the abiss. \nThankfully there's a path back to the training ground.\nYou return claiming a trick question is why you denied access to the brideg of death.")
            input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
            print(colorama.Style.RESET_ALL)
            new_result = Result(
                knight_id = current_knight_id,
                quest_id = 2,
                outcome = "loss"
                )
            session.add(new_result)
            session.commit()
            in_program = False
            training_ground(session, knight_full_title, knight_short_title, current_knight_id)

        else:
            print("Answer the question! Select A or B\n")
            bridge_1_input
        


# Sir Galahad the Chaste 	What is your name?	
# Bridge of Death	Sir Galahad of Camelot	Tim the Enchanter 
# 	What is your quest?	
# 	To seek the Holy Grail	Return to the castle of Anthrax
# 	What is your favorite color?	
# 	Yellow	Blue