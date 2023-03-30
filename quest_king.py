from sqlalchemy import *
from sqlalchemy.orm import *
from tables import Result
from training_ground import training_ground

def quest_king(session, knight_full_title, knight_short_title, current_knight_id):
    print(
        '''
                                     o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                  o
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$$
        ''')
    print("Defend your King!")
    pass

    in_program = True
    input("\n Click enter/return to continue \n")
    print("Arthur, King of the Britons, is a great ruler appointed by the Lady of the Lake when she handed him the Excalibur sword. \nThis is clearly a way to find establish a monarch and should never be questioned. \nAs a citizen in King Arthur's domain, you are tasked with risking life and limb to protect your king. \nIn this quest, you must advice the King in order to help him avoid danger.")
    input("\n Click enter/return to continue \n")
    print("You and the King have travelled together touring his kingdom when his trusty steed dies. \nThe only way for you to continue with the journey is with the sound effect of hoof beats - thus, coconuts are required! \nWhat is the best way to transport the tropical fruit to you in England?")
    while in_program:
        king_1_input = input(f"     A) European Swallow\n     B) African Swallow\n(A / B) ").lower()
        if king_1_input == "b":
            #Correct
            print("Of course! If you look at the weight ratios, a 5oz European Swallow would be much too small. \nThe larger African Swallow could complete this task without falling from the sky. You must be well studied in physics.")
            input("\n Click enter/return to continue \n")
            print("You and the king approach a castle and ask if there are any noble knights that would like to join the knights of the round table.")
            input("\n Click enter/return to continue \n")
            print(f"Watch out {knight_short_title}! As you approach the castle occupied it becomes clear that it is occupied by the French, as they begin to fling livestock at you and the King! \nKing Arthur asks you what should be the course of action.")
            king_2_input = input("     A) RUN AWAY!\n     B) Throw the minstrel at them (the music wasn't that good anyways)\n(A / B) ")
            if king_2_input == "a":
                #Correct
                print("Yes, running away is the most nobel way to battle. Well chosen.")
                input("\n Click enter/return to continue \n")
                print("You and King Arthur enter into the woods on your journey and are surrounded by the most vicious of villians - The Knights Who Say NI!\nThe knights begin to attack by shouting NI at you (and occasionally Ping and Nuu-Wom!)\nYou plead for them to spare your life and they argree, but only if you bring them a [dramatic chord] shrubbery!")
                input("\n Click enter/return to continue \n")
                print("You venture into the village and find the finest shurbbery in all of the land and bring it back to the knights.")
                input("\n Click enter/return to continue \n")
                print("The Knights who say NI are not happy with the shrubbery offering. \nThe only choice is to engage in battle with the merciless knights. \nWhat is your best tacktical approach?")
                king_3_input = input("     A) No way to tell\n     B) It is hard to say\n(A / B )")
                if king_3_input == "b":
                    #Correct 
                    print(f"But of course {knight_full_title}! IT is the most damaging word to the Knights who say NI.\nThey shrivel into sniffling children as you walk past them.")
                    input("\n Click enter/return to continue \n")
                    print("The king has seen enough to trust your judgment and thanks you for helping him complete this portion of the quest. \nYour return to the training ground.")
                    input("\n Click enter/return to continue \n")
                    new_result = Result(
                        knight_id = current_knight_id,
                        quest_id = 3,
                        outcome = "win"
                    )
                    session.add(new_result)
                    session.commit()
                    in_program = False
                    training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                    pass
                elif king_3_input == "a":
                    #Incorrect 
                    print("No way to tell? No way to tell?!? You can't tell the king that you don't know! \nClearly you need more training on how to combat the Knights who say Ni. \nYou return to the training grounds and leave King Arthur to continue his quest without you.")
                    input("\n Click enter/return to continue \n")
                    new_result = Result(
                        knight_id = current_knight_id,
                        quest_id = 3,
                        outcome = "loss"
                    )
                    session.add(new_result)
                    session.commit()
                    in_program = False
                    training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                    pass
                else:
                    print("Answer the question! Select A or B\n")
            elif king_2_input == "b":
                #Incorrect
                print(f"{knight_full_title}, you would sacrafice our minstral to live with the french?\nAs a benevolent king, I cannot force that cruel punishment upon any of my subjects!\n(under his breath) even if his music was redundant and lacked imagination\n")
                input("\n Click enter/return to continue \n")
                print("King Arthur tells you to be gone! And as punishment, you must walk with the minstral all the way back to the training grounds.")
                input("\n Click enter/return to continue \n")
                new_result = Result(
                    knight_id = current_knight_id,
                    quest_id = 3,
                    outcome = "loss"
                )
                session.add(new_result)
                session.commit()
                in_program = False
                training_ground(session, knight_full_title, knight_short_title, current_knight_id)
            else:
                print("Answer the question! Select A or B\n")
        elif king_1_input == "a":
            print("What? An English Swallow carry a coconut all the way from the tropics? \nIt's a matter of weight ratios! A 5 ounce bird couldn't carry a 1 pound coconut.\nClearly you are not a trusted source to advice the king if you do not understand basic bird math.")
            input("\n Click enter/return to continue \n")
            print("The French and King Arthur laugh at you as you return to the training ground. \nYou hear in the background 'I bet their mother was a hamster and their father smells of elderberries!'" )
            input("\n Click enter/return to continue \n")
            new_result = Result(
                knight_id = current_knight_id,
                quest_id = 3,
                outcome = "loss"
            )
            session.add(new_result)
            session.commit()
            in_program = False
            training_ground(session, knight_full_title, knight_short_title, current_knight_id)
                    
            pass
            #Incorrect
        else:
            print("Answer the question! Select A or B\n")