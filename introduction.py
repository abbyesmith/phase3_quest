from sqlalchemy import *
from sqlalchemy.orm import *
from tables import Knight
from tables import Quest
from quest_bridge import quest_bridge
from quest_witch import quest_witch
from quest_king import quest_king


def introduction(session, current_user_id):
    logged_in = True
    print("To begin, you must create your knight that who's ambition is to join the knights of the round table in King Arthur's court. \n For example, Sir Lancelot the Brave of Camelot is a knight sitting at the round table.")
    knight_name_input = input("Knight's First Name: ").title()
    checking_knight_names = session.query(Knight).filter(Knight.name == knight_name_input).first()
    if checking_knight_names:
        # ERROR HERE - 1) This should load a game
        # 2) It is terminating the game
        print (f"A knight by the name of {knight_name_input} has already gone out on this holy quest. Please select a new name for your knight.")
    else: 
        knight_adjective_input = input("What is one adjective that describes your knight? ").title()
        knight_gender_input = input("What is your knight's gender? (male / female / other) ").lower()
        knight_location_input = input("What is your knight's location? ").title()
        if knight_gender_input == "male":
            knight_full_title = f"Sir {knight_name_input} the {knight_adjective_input} of {knight_location_input}"
            knight_short_title = f"Sir {knight_name_input} the {knight_adjective_input}"
        if knight_gender_input == "female":
            knight_full_title = f"Lady {knight_name_input} the {knight_adjective_input} of {knight_location_input}"
            knight_short_title = f"Lady {knight_name_input} the {knight_adjective_input}"
        if knight_gender_input == "other":
            knight_full_title = f"Noble {knight_name_input} the {knight_adjective_input} of {knight_location_input}"
            knight_short_title = f"Noble {knight_name_input} the {knight_adjective_input}"
    new_knight = Knight(
        user_info_id = current_user_id, 
        name = knight_name_input,
        adjective = knight_adjective_input,
        gender = knight_gender_input,
        location = knight_location_input
        )
    session.add(new_knight)
    session.commit()
    # current_user_id = session.query(User_Info.id).filter_by(username = username_input).scalar()
    current_knight_id = session.query(Knight.id).filter_by(name = knight_name_input).scalar()
    print(
        '''
\n 
\n 
\n 
\n 
\n 
\n 
\n 
\n 
   _________
  |o^o^o^o^o|
  {   _!_   }
   \   !   /
    `.   .'
      )=(
     ( + )
      ) (
  .--'   `--.
  `---------'
        '''
    )
    print(f"Greetings {knight_full_title}! We have been looking for a knight with your abilities to assist Arthur, King of the Britons, on his quest for the holy grail.\n")
    input("\n Click enter/return to continue \n")
    print(f"{knight_short_title}, in order to earn a seat at King Arthur's round table of knights, \nyou must successfully complete 2 quests with the following heroic knights and 1 with the Good King himself!") 
    input("\n Click enter/return to continue \n")
    print("It is your choice on the order to complete the quests. \nIf you fail a quest, you will be brought back to the training yard to restart the quest or select a different quest. \nWhen you successfully complete a quest, you will return to the training yard to select a new quest. \n Upon successful completion of the three quests, you will be awarded a coveted seat at King Arthur's Round Table!")
    input("\n Click enter/return to continue \n")
    # def show_quests():
    quests = session.query(Quest).all()

    # for quest in quests:
    #     print(f" - {quest.__repr__()}")
    print("QUESTS")
    for i, quest in enumerate(quests):
        print(f"\n{i+1} - {quest.title} with {quest.character}")

    quest_selector = input(f"\nSelect the first quest you wish to complete (1 / 2 / 3) \n")
    
    if quest_selector == "1":
        logged_in = False
        quest_witch(session, knight_full_title, knight_short_title, current_knight_id)
        pass
    elif quest_selector == "2":
        logged_in = False
        quest_bridge(session, knight_full_title, knight_short_title, current_knight_id)
        pass
    elif quest_selector == "3":
        logged_in = False
        quest_king(session, knight_full_title, knight_short_title, current_knight_id)
        pass
    else:
        print(f"{quest_selector} is not a valid quest")

# class Knight(Base):
#     __tablename__ = 'knight'
#     id = Column(Integer(), primary_key = True)
#     user_info_id = Column(Integer(), ForeignKey("user_info.id"))
#     name = Column(String())
#     adjective = Column(String())
#     gender = Column(String())
#     location = Column(String())