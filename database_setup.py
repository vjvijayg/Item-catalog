from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class FoodChart(Base):
    __tablename__ = 'food_Chart'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    protein = Column(String(8))
    carbs = Column(String(8))
    fats = Column(String(8))
    calories = Column(String(8))
    amount = Column(String(20))
    ftype = Column(String(20))
    food_id = Column(Integer, ForeignKey('food.id'))
    food = relationship(Food)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'protein': self.protein,
            'carbs' : self.carbs,
            'fats': self.fats,
            'calories': self.calories,
            'amount' : self.amount,
            'ftype' : self.ftype,
        }


engine = create_engine('sqlite:///nutrition.db')


Base.metadata.create_all(engine)
