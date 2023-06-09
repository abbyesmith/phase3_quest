import threading
import sys
import colorama
from sqlalchemy import *
from sqlalchemy.orm import *
from playsound import playsound
from tables import Round_Table


def play_sound():
    playsound('/Users/abbysmith/Development/code/phase-3/phase3_quest/the-knights-at-camelot-singing-the-entire-knights-of-the-round-table-song.mp3')

def round_table(session, knight_full_title, knight_short_title, successful_quest_id_array, result_array):
    logged_in = True
    while logged_in:
        print(f"Kneel before your king, {knight_short_title}")
        input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
        print(colorama.Style.RESET_ALL)
        print(f"I name thee {knight_full_title}, KNIGTH OF THE ROUND TABLE")
        input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
        print(colorama.Style.RESET_ALL)
        
        sound_thread = threading.Thread(target=play_sound)
        sound_thread.start()        
        
        print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT +
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
        
        print(colorama.Style.RESET_ALL)
        print("Arise and join your fellow knights in merriment and song!")
        input(colorama.Fore.CYAN + "\n Click enter/return to continue \n")
        print(colorama.Style.RESET_ALL)
        print(f"{knight_full_title}, it took you {len(result_array)} attempts to complete the three quests in order to join the knights of the round table.\nSee how well you did compared with your fellow knights:")
        round_table_rows = session.query(Round_Table).all()
        for row in round_table_rows:
            print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT +row.__repr__())
        # logged_in = False
        input(colorama.Fore.CYAN + "\n Click enter/return \n")
        print(colorama.Style.RESET_ALL)
        print("\nYou have won the game. The program will automatically close once the song is finished.\n")
        sys.exit(0)
        


        
    