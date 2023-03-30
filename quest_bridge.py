from sqlalchemy import *
from sqlalchemy.orm import *
from tables import Result
from training_ground import training_ground

def quest_bridge(session, knight_full_title, knight_short_title, current_knight_id):
    print(
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
    in_program = True
    while in_program:
        input("\n Click enter/return to continue \n")
        print("The holy grail has been rumored to be in the Castle of AARGH, \nwhich can only be reach by crossing the \n DUN DUN DUUUUN \n BRIDGE OF DEATH.")
        input("\n Click enter/return to continue \n")
        print("The great and powerful enchanter is gaurding the bridge and will only allow you to cross if you and Sir Galahad can answer these question five (no three).")
        input("\n Click enter/return to continue \n")
        print("Question 1: What is your name?")
        
        bridge_1_input = input(f"     A) Sir Galahad the Chaste and {knight_short_title} \n     B) Tim the Enchanter\n(A / B) ").lower()
        if bridge_1_input == "a":
            print("Correct, but don't be too proud of yourself. Even a 2 year old knows how to do that")
            input("\n Click enter/return to continue \n")
            print("Question2: What is your quest?")
            
            bridge_2_input = input("     A) To seek the Holy Grail\n     B) Return to the Castle of Anthrax\n(A / B) ")
            if bridge_2_input == "a":
                print("We have a good little knight on our hands here who listens to the mission!")
                input("\n Click enter/return to continue \n")
                print("Question 3: What is your favorite color?")
                bridge_3_input = input("     A) Blue\n     B) Yellow\n(A / B ) ")
                if bridge_3_input == "b":
                    #Correct -- REMEMBER THE ANSWER IS YELLOW
                    print("You know your name, quest and favorite color?!? Wooza! You are clearly one of the most integent knights in this land.\nYou may cross the bridge to continue the quest for the holy grail.")
                    input("\n Click enter/return to continue \n")
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
                    input("\n Click enter/return to continue \n")
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
                input("\n Click enter/return to continue \n")
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
            input("\n Click enter/return to continue \n")
            print("Tim the Enchantor explodes you off the cliff edge into the abiss. \nThankfully there's a path back to the training ground.\nYou return claiming a trick question is why you denied access to the brideg of death.")
            input("\n Click enter/return to continue \n")
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