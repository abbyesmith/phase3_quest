from sqlalchemy import *
from sqlalchemy.orm import *
import colorama
from playsound import playsound
from tables import Result
from tables import Quest
from tables import Round_Table
# This is creating a circular error, double check out more at bottom of code
# from quest_bridge import quest_bridge
# from quest_witch import quest_witch
# from quest_king import quest_king
from round_table import round_table

def training_ground(session, knight_full_title, knight_short_title, current_knight_id):
    logged_in = True
    while logged_in:
        print(
        '''
    n                                                                 :.
    E%                                                                :"5
    z  %                                                              :" `
    K   ":                                                           z   R
    ?     %.                                                       :^    J
    ".    ^s                                                     f     :~
    '+.    #L                                                 z"    .*
      '+     %L                                             z"    .~
        ":    '%.                                         .#     +
          ":    ^%.                                     .#`    +"
            #:    "n                                  .+`   .z"
              #:    ":                               z`    +"
                %:   `*L                           z"    z"
                  *:   ^*L                       z*   .+"
                    "s   ^*L                   z#   .*"
                       #s   ^%L               z#   .*"
                        #s   ^%L           z#   .r"
                           #s   ^%.       u#   .r"
                            #i   '%.   u#   .@"
                              #s   ^}u#   .@"
                                #s x#   .*"
                                x#`  .@%.
                              x#`  .d"  "%.
                            xf~  .r" #s   "%.
                      u   x*`  .r"     #s   "%.  x.
                      %Mu*`  x*"         #m.  "%zX"
                      :R(h x*              "h..*dN.
                    u@NM5e#>                 7?dMRMh.
                  z$@M@$#"#"                 *""*@MM$hL
                 u@@MM8*                          "*$M@Mh.
                z$RRM8F"                             "N8@M$bL
                5`RM$#                                  'R88f)R
                'h.$"                                     #$x*
            ''')
        print("WELCOME TO THE TRAINING GROUNDS")
        input(colorama.Fore.CYAN + "\n Click any key to continue \n")
        print(colorama.Style.RESET_ALL)
        last_outcome = session.query(Result).filter(Result.knight_id == current_knight_id).order_by(desc(Result.id)).first()
        if last_outcome.outcome == "loss":
            print(f"{knight_short_title}, you are a disgrace who should be shunned to fields to shovel the cow waste. \n Fortunatly for you, King Arthur sees promise in you and will allow you to continue your journey to joining the knights of the round table.")
        else:
            print(f"{knight_full_title} - We stand in awe of your valure and marvel in your success!")
            print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT +
                '''             
               \  :  /
            `. __/ \__ .'
            _ _\     /_ _
              ./_   _\.
             .'  \ /  `.
               /  :  \    
                    
                '''
                )
            playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/success-fanfare-trumpets-6185.mp3')
        results = session.query(Result).filter(Result.knight_id == current_knight_id).all()
        # print(results)
        result_array = [results.outcome for results in results]
        # print(result_array)
        successful_quest_id_array = [results.quest_id for results in results if results.outcome == "win"] 
        # print(successful_quest_id_array)
        if len(successful_quest_id_array) == 3:
            print(f"Congratulations {knight_full_title}!!!!!! /n You have successfully completed three quests and have earned your seat at King Arthur's Round Table!")
            print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT +
            '''
                         _^_
                        / | \.
                       |.-=-.|
                       )\_|_/(
                    .=='\   /`==.
                 .'\    (`:')   /`.
               _/_ |_ .-' : `-._|__\_
              <___>' \    :   / `<___>
              /  /    >=======<  /  /
            _/ .'    /  ,-:-.  \/=,'
           / _/     |__/v^v^v\__) \.
            \(\)     |V^V^V^V^V|\_/
            (\ \     \`---|---'/
              \ \     \-._|_,-/
               \ \     |__|__|
                \ \   <___X___>
                 \ \   \..|../
                  \ \   \ | /
                   \ \  /V|V\.
                    \ |/  |  \.
                      '--' `--`  
                ''')
            print(f"Newest Member of King Arthur's Round Table: \n{knight_full_title}")
            print(colorama.Style.RESET_ALL)
            new_member = Round_Table(
                knight_id = current_knight_id,
                knight_full_name = knight_full_title,
                attempts = len(result_array)
            )
            session.add(new_member)
            session.commit()

            logged_in = False
            round_table(session, knight_full_title, knight_short_title, 
            successful_quest_id_array, result_array)
        else:
            input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
            print(colorama.Style.RESET_ALL)
            if len(successful_quest_id_array) == 2:
                print(f"{knight_short_title}, you are one brave and successful quest away from the greatest honor of your life. \nDon't let King Arthur down now! Select the last quest to change history!")
            elif len(successful_quest_id_array) == 1:
                print(f"{knight_short_title}, you have successfully completed one quest. Continue your journey to try your new quest")
            elif len(successful_quest_id_array) == 0:
                print(f"{knight_short_title}, you have yet to complete a quest successfully. \nKing Arthur requires you to persist until you have completed all 3 quests if you wish to join the knights of the round table.")
            else:
                print("The game is broken. Please try again")
        
        # Remaining quests:
        print("Remaining quests:\n")
        all_quests = session.query(Quest).all()

        for quest in all_quests:
            if quest.id not in successful_quest_id_array:
                print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT +f"     - {repr(quest)}")
                print(colorama.Style.RESET_ALL)

        quest_selector = input(colorama.Fore.GREEN + colorama.Style.BRIGHT +"\nSelect the quest you wish to complete from the list above\n")
        print(colorama.Style.RESET_ALL)
        
        if quest_selector == "1":
            logged_in = False
            from quest_witch import quest_witch 
            quest_witch(session, knight_full_title, knight_short_title, current_knight_id)
            
        elif quest_selector == "2":
            logged_in = False
            from quest_bridge import quest_bridge
            quest_bridge(session, knight_full_title, knight_short_title, current_knight_id)
            
        elif quest_selector == "3":
            logged_in = False
            from quest_king import quest_king
            quest_king(session, knight_full_title, knight_short_title, current_knight_id)
            
        else:
            print(f"{quest_selector} is not a valid quest")
            quest_selector


