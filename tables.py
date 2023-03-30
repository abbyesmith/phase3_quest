from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()

class Quest(Base):
    __tablename__ = 'quest'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    character = Column(String())
    result = relationship('Result', backref = 'quest')

    def __repr__(self):
        return f"Quest {self.id}: {self.title}, {self.character}"

class User_Info(Base):
    __tablename__ = 'user_info'
    id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String())
    knight = relationship('Knight', backref = 'user_info')

    def __repr__(self):
        return f"{self.username}"

class Knight(Base):
    __tablename__ = 'knight'
    id = Column(Integer(), primary_key = True)
    user_info_id = Column(Integer(), ForeignKey("user_info.id"))
    name = Column(String())
    adjective = Column(String())
    gender = Column(String())
    location = Column(String())

class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer(), primary_key=True)
    knight_id = Column(Integer(), ForeignKey('knight.id'))
    quest_id = Column(Integer(), ForeignKey('quest.id'))
    outcome = Column(String())

class Round_Table(Base):
    __tablename__ = 'round_table'
    id = Column(Integer(), primary_key=True)
    knight_id = Column(Integer(), ForeignKey('knight.id'))
    knight_full_name = Column(String())
    attempts = Column(Integer())

    def __repr__(self):
        return f"{self.knight_full_name} Score: {self.attempts}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///tables.db')
    # Round_Table.__table__.drop(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
    #     new_quest_data = Quest(
    #         title = "Defend your King",
    #         character = "Arthur, King of the Britions"
    #     )
    #     print(new_quest_data)
    #     session.add(new_quest_data)
        session.commit()

# To delete a user from the db
# def delete(name_delete):
#     engine = create_engine('sqlite:///tables.db')
#     with Session(engine) as session:
#         session.query(User_Info).filter(User_Info.username == name_delete).delete()
#         session.commit()

# delete("Trial")
