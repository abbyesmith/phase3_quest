import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from playsound import playsound
from tables import Round_Table

def round_table(session, knight_full_title, knight_short_title, successful_quest_id_array, result_array):
    logged_in = True
    while logged_in:
        print(f"Kneel before your king, {knight_short_title}")
        input("\n Click enter/return to continue \n")
        print(f"I name thee {knight_full_title}, KNIGTH OF THE ROUND TABLE")
        input("\n Click enter/return to continue \n")
        playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/the-knights-at-camelot-singing-the-entire-knights-of-the-round-table-song.mp3')
        print(
        '''
                                                                |\/\/\/\/|
                                                                '========'
                                                                (_ SSSSSSs
                                                                )a'`SSSSSs
                                                               /_   SSSSSS
                                                               .=## SSSSS
                                                               .####  SSSSs
                                                               ###::::SSSSS
                                                              .;:::""""SSS
                                                             .:;:'  . .  \.
                                                            .::/  '     .'|
                                                           .::( .         |
                                                           :::)           \.
                                                           /\(            /
                                                          /)            ( |
                                                        .'  \  .       ./ /
                                                     _-'    |\  .        |
                                   _..--..   .  /"---\      | ` |      . |
           -=====================,' _     \=(*#(7.#####()   |  `/_..   , (
                       _.-''``';'-''-) ,.  \ '  '+/// |   .'/   \  ``-.) \.
                     ,'  _.-  ((    `-'  `._\    `` \_/_.'  )    /`-._  ) |
                   ,'\ ,'  _.'.`:-.    \.-'                 /   <_L   )"  |
                 _/   `._,' ,')`;  `-'`'                    |     L  /    /
                / `.   ,' ,|_/ / \                          (    <_-'     \.
                \ / `./  '  / /,' \                        /|`         `. |
                )\   /`._   ,'`._.-\                       |)            \.'
               /  `.'    )-'.-,' )__)                      |\            `|
              : /`. `.._(--.`':`':/ \                      ) \             \.
              |::::\     ,'/::;-))  /                      ( )`.            |
              ||:::::  . .::':  :`-(                       |/    .          |
              ||::::|  . :|  |==[]=:                       .        -       \.
              |||:::|  : ||  :  |  |                      /\           `     |
  ___ ___     '|;:::|  | |'   \=[]=|                     /  \                \.
 |   /_  ||``|||:::::  | ;    | |  |                     \_.'\_               `-.
 :   \_``[]--[]|::::'\_;'     )-'..`._                 .-'\``:: ` .              \.
  \___.>`''-.||:.__,'        |_______`>              <_____:::.         . . \  _/
                                                            `+...............
        ''')
        
        print("Arise and join your fellow knights in merriment and song!")
        input("\n Click enter/return to continue \n")
        print(f"{knight_full_title}, it took you {len(result_array)} attempts to complete the three quests in order to join the knights of the round table.\nSee how well you did compared with your fellow knights:")
        round_table_rows = session.query(Round_Table).all()
        for row in round_table_rows:
            print(row.__repr__())
        logged_in = False
        sys.exit(0)
        


        
    