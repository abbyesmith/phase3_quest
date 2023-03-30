from sqlalchemy import *
from sqlalchemy.orm import *
from tables import User_Info
from introduction import introduction

if __name__ == '__main__':
    engine = create_engine('sqlite:///tables.db')
    print(
        '''
   ____                 _      __              _   _          
  /___ \_   _  ___  ___| |_   / _| ___  _ __  | |_| |__   ___ 
 //  / / | | |/ _ \/ __| __| | |_ / _ \| '__| | __| '_ \ / _ |
/ \_/ /| |_| |  __/\__ \ |_  |  _| (_) | |    | |_| | | |  __/
\___,_\ \__,_|\___||___/\__| |_|  \___/|_|     \__|_| |_|\___|
                                                              
             _           ___           _ _ 
  /\  /\___ | |_   _    / _ \_ __ __ _(_) |
 / /_/ / _ \| | | | |  / /_\/ '__/ _` | | |
/ __  / (_) | | |_| | / /_ \| | | (_| | | |
\/ /_/ \___/|_|\__, | \____/|_|  \__,_|_|_|
               |___/                                         
        '''
    )
    with Session(engine) as session:
        in_program = True

        print("Welcome brave soul! You are entering into the land of King Arthur who needs your help in the quest for the holy grail.")
        while in_program:
            start_input = input("Are you signing in as a new user or an existing player? (new / existing / not sure) ").lower()
            # user input resolved
            if start_input == "new":
                username_input = input("Welcome noble knight! Please enter a unique username: ")
                checking_usernames = session.query(User_Info).filter(User_Info.username == username_input).first()
                if checking_usernames:
                    print(f"The username {username_input} already exists. Please select a unique username.")
                else:
                    new_password = input("Create Password: ")
                    new_user = User_Info(username=username_input, password=new_password)
                    session.add(new_user)
                    session.commit()
                    print(f"Success! Username: {username_input} Password: {new_password}")
                    # current_user_id is the id of the user that will be needed to link their account to their knights on the next page
                    current_user_id = session.query(User_Info.id).filter_by(username = username_input).scalar()
                    in_program = False
                    introduction(session, current_user_id)
                    # THIS PATH IS DONE

            elif start_input == "existing":
                print("\n Log in")
                username_input = input("Enter your username: \n")
                checking_usernames = session.query(User_Info).filter(User_Info.username == username_input).first()
                if checking_usernames:
                    print(f"\nWelcome back {username_input}!")
                    # current_user_id is the id of the user that will be needed to link their account to their knights on the next page
                    current_user_id = session.query(User_Info.id).filter_by(username = username_input).scalar()
                    password_attempt = True
                    while password_attempt:
                        password_input = input("\nEnter your password: \n")
                        correct_password = checking_passwords = session.query(User_Info).filter(User_Info.password == password_input).first()
                        if correct_password:
                            print("\nLog in successful")
                            input("\n Click enter/return to continue \n")
                            in_program = False
                            introduction(session, current_user_id)
                            password_attempt = False
                        else:
                            print(f"Error: {password_input} is not your password")
                            update_password_input = input("Would you like to reset your password? (yes / no)").lower()
                            if update_password_input == "yes":
                                new_password = input("Please enter your new password: ")
                                user = session.query(User_Info).filter_by(username=username_input).first()
                                user.password = new_password
                                session.commit()
                                password_attempt = False
                                print(f"\nPassword successfully changed.\nUsername: {username_input} Password: {new_password}\n")
                                input("\n Click enter/return to continue \n")
                                in_program = False
                                introduction(session, current_user_id)
                                # THIS OPTION IS DONE
                                pass
                            else:
                                input("Press enter to retry your password")
                                # THIS OPTION IS DONE
                else:
                    print("That is not a valid username. Here are the usernames that already exist: ")
                    all_users = session.query(User_Info).all()
                    print(f"{all_users}")

            elif start_input == "not sure":
                print("Ahh, ye of little memory. Here are the list of users who have agreed for this holy quest:")
                all_users = session.query(User_Info).all()
                print(f"Existing Usernames: {all_users}")
                # Done

            else:
                print("Invalid input: " + start_input + "type one of the following (new / existing / not sure)")
                start_input
                # Done