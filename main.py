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
                new_username = input("Welcome noble knight! Please enter a unique username: ")
                checking_usernames = session.query(User_Info).filter(User_Info.username == new_username).first()
                if checking_usernames:
                    print(f"The username {new_username} already exists. Please select a unique username.")
                else:
                    new_password = input("Password: ")
                    new_user = User_Info(username=new_username, password=new_password)
                    session.add(new_user)
                    session.commit()
                    print(f"Success! Username: {new_username} Password: {new_password}")
                    in_program = False
                    introduction(session)
                    # THIS PATH IS DONE

            elif start_input == "existing":
                print("\n Log in")
                username_input = input("Enter your username: \n")
                checking_usernames = session.query(User_Info).filter(User_Info.username == username_input).first()
                if checking_usernames:
                    print(f"Welcome back {username_input}!")
                    password_input = input("Enter your password: \n")
                    checking_passwords = session.query(User_Info).filter(User_Info.password == password_input).first()
                    if checking_passwords:
                        print("Log in successful")
                        in_program = False
                        introduction(session)
                    else:
                        print(f"Error: {password_input} is not your password")
                        # THIS OPTION IS DONE
                        # If time, give an option to do a .update to change the password
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
                # Done