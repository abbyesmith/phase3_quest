def quest_king(session, knight_full_title, knight_short_title):
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
    # input("\n Click enter/return to continue \n")
    # print("The holy grail has been rumored to be in the Castle of AARGH, \nwhich can only be reach by crossing the \n DUN DUN DUUUUN \n BRIDGE OF DEATH.")
    # input("\n Click enter/return to continue \n")
    # print("The great and powerful enchanter is gaurding the bridge and will only allow you to cross if you and Sir Galahad can answer these question five (no three).")
    # input("\n Click enter/return to continue \n")
    # print("WHAT is your name?")
    while in_program:
        bridge_1_input = input(f"     A) Sir Galahand the Chaste and {knight_short_title} \n     B) Tim the Enchanter\n(A / B) ").lower()
        if bridge_1_input == "a":
            pass
            #Correct
            bridge_2_input = input("     A) To seek the Holy Grail\n     B) To win a CLI game\n(A / B) ")
            if bridge_2_input == "a":
                #Correct
                pass
                print("What is your favorite color?")
                bridge_3_input = input("     A) Blue\n     B) Yellow\n(A / B )")
                if bridge_3_input == "b":
                    #Correct -- REMEMBER THE ANSWER IS YELLOW
                    pass
                elif bridge_3_input == "a":
                    #Incorrect -- REMEMBER THE ANSWER IS YELLOW, not blue
                    pass
                else:
                    print("Answer the question! Select A or B\n")
            elif bridge_2_input == "b":
                #Incorrect
                pass
            else:
                print("Answer the question! Select A or B\n")
        elif bridge_1_input == "b":
            pass
            #Incorrect
        else:
            print("Answer the question! Select A or B\n")