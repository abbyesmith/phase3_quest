from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

class Quest(Base):
    __tablename__ = 'quest'
    id = Column(Integer, primary_key=True)
    titles = Column(String())
    character = Column(String())

    def __repr__(self):
        return f"Quest {self.id}: {self.titles}, {self.character}"

class User_Info(Base):
    __tablename__ = 'user_info'
    id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String())

    def __repr__(self):
        return f"{self.username}"
    
if __name__ == '__main__':
    engine = create_engine('sqlite:///quest.db')
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        new_user_data = User_Info(
            username = "Abby",
            password = "Abby"
        )
        print(new_user_data)
        session.add(new_user_data)
        session.commit()