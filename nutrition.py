from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Food, Base, FoodChart, User

engine = create_engine('sqlite:///nutrition.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Vijay Kumar", email="forevervijju@gmail.com",
             picture="https://avatars1.githubusercontent.com/u/25880067?v=3&u=355d1bcf8d75f01f4817098d8fd5ec2dd43b4acf&s=400")
session.add(User1)
session.commit()


# Fruits list with nutional content
food = Food(user_id=1, name="Foods")

session.add(food)
session.commit()


foodChart1 = FoodChart(user_id=1, name="Bananas", protein="1.1g", carbs="23g",
                       fats="0.3g", calories="89", amount="Per 100 grams",
                       ftype="Fruits", food=food)

session.add(foodChart1)
session.commit()


foodChart2 = FoodChart(user_id=1, name="Apples", protein="0.3g", carbs="14g",
                       fats="0.2g", calories="52", amount="Per 100 grams",
                       ftype="Fruits", food=food)

session.add(foodChart2)
session.commit()


foodChart3 = FoodChart(user_id=1, name="Oranges", protein="0.9g", carbs="12g",
                       fats="0.1g", calories="47", amount="Per 100 grams",
                       ftype="Fruits", food=food)

session.add(foodChart3)
session.commit()


foodChart4 = FoodChart(user_id=1, name="Pomegranates", protein="1.7g", carbs="19g",
                       fats="1.2g", calories="83", amount="Per 100 grams",
                       ftype="Fruits", food=food)

session.add(foodChart4)
session.commit()



foodChart5 = FoodChart(user_id=1, name="Potatoes", protein="2g", carbs="17g",
                       fats="0.1g", calories="77", amount="Per 100 grams",
                       ftype="Root Vegetables", food=food)

session.add(foodChart5)
session.commit()


foodChart6 = FoodChart(user_id=1, name="Carrots", protein="0.9g", carbs="10g",
                       fats="0.2g", calories="41", amount="Per 100 grams",
                       ftype="Root Vegetables", food=food)

session.add(foodChart6)
session.commit()


foodChart7 = FoodChart(user_id=1, name="Raddishes", protein="0.7g", carbs="3.4g",
                       fats="0.1g", calories="16", amount="Per 100 grams",
                       ftype="Root Vegetables", food=food)

session.add(foodChart7)
session.commit()


foodChart8 = FoodChart(user_id=1, name="Beetroots", protein="1.6g", carbs="10g",
                       fats="0.2g", calories="43", amount="Per 100 grams",
                       ftype="Root Vegetables", food=food)

session.add(foodChart8)
session.commit()



foodChart9 = FoodChart(user_id=1, name="Tomatoes", protein="0.9g", carbs="3.9g",
                       fats="0.2g", calories="18", amount="Per 100 grams",
                       ftype="Vegetables", food=food)

session.add(foodChart9)
session.commit()


foodChart10 = FoodChart(user_id=1, name="Brinjal", protein="1g", carbs="6g",
                       fats="0.2g", calories="25", amount="Per 100 grams",
                       ftype="Vegetables", food=food)

session.add(foodChart10)
session.commit()


foodChart11 = FoodChart(user_id=1, name="Ladies fingers", protein="1.9g", carbs="7g",
                       fats="0.2g", calories="33", amount="Per 100 grams",
                       ftype="Vegetables", food=food)

session.add(foodChart11)
session.commit()


foodChart12 = FoodChart(user_id=1, name="Broccoli", protein="2.8g", carbs="7g",
                       fats="0.4g", calories="34", amount="Per 100 grams",
                       ftype="Vegetables", food=food)

session.add(foodChart12)
session.commit()


foodChart13 = FoodChart(user_id=1, name="Mushrooms", protein="3.1g", carbs="3.3g",
                       fats="0.3g", calories="22", amount="Per 100 grams",
                       ftype="Vegetables", food=food)

session.add(foodChart13)
session.commit()


foodChart14 = FoodChart(user_id=1, name="Spinach", protein="2.9g", carbs="3.6g",
                       fats="0.4g", calories="23", amount="Per 100 grams",
                       ftype="Leaf Vegetables", food=food)

session.add(foodChart14)
session.commit()


foodChart15 = FoodChart(user_id=1, name="Kale", protein="4.3g", carbs="9g",
                       fats="0.9g", calories="49", amount="Per 100 grams",
                       ftype="Leaf Vegetables", food=food)

session.add(foodChart15)
session.commit()


foodChart16 = FoodChart(user_id=1, name="Mustard Greens", protein="2.9g", carbs="4.7g",
                       fats="0.4g", calories="27", amount="Per 100 grams",
                       ftype="Leaf Vegetables", food=food)

session.add(foodChart16)
session.commit()


foodChart17 = FoodChart(user_id=1, name="Chard", protein="1.8g", carbs="3self.7g",
                       fats="0.2g", calories="19", amount="Per 100 grams",
                       ftype="Leaf Vegetables", food=food)

session.add(foodChart17)
session.commit()


foodChart18 = FoodChart(user_id=1, name="Mung Beans", protein="24g", carbs="63g",
                       fats="1.2g", calories="347", amount="Per 100 grams",
                       ftype="Lentils", food=food)

session.add(foodChart18)
session.commit()


foodChart19 = FoodChart(user_id=1, name="Kidney Beans", protein="24g", carbs="60g",
                       fats="0.8g", calories="333", amount="Per 100 grams",
                       ftype="Lentils", food=food)

session.add(foodChart19)
session.commit()


foodChart20 = FoodChart(user_id=1, name="Pigeon Peas", protein="22g", carbs="63g",
                       fats="1.5g", calories="343", amount="Per 100 grams",
                       ftype="Lentils", food=food)

session.add(foodChart20)
session.commit()


foodChart21 = FoodChart(user_id=1, name="Soya Bean", protein="36g", carbs="30g",
                       fats="20g", calories="446", amount="Per 100 grams",
                       ftype="Lentils", food=food)

session.add(foodChart21)
session.commit()



foodChart22 = FoodChart(user_id=1, name="Chicken", protein="31g", carbs="0g",
                       fats="3.6g", calories="167", amount="Per 100 grams",
                       ftype="Meat", food=food)

session.add(foodChart22)
session.commit()


foodChart23 = FoodChart(user_id=1, name="Mutton", protein="25g", carbs="0g",
                       fats="21g", calories="294", amount="Per 100 grams",
                       ftype="Meat", food=food)

session.add(foodChart23)
session.commit()


foodChart24 = FoodChart(user_id=1, name="Fish", protein="22g", carbs="0g",
                       fats="12g", calories="206", amount="Per 100 grams",
                       ftype="Meat", food=food)

session.add(foodChart24)
session.commit()


foodChart25 = FoodChart(user_id=1, name="Pork", protein="27g", carbs="0g",
                       fats="14g", calories="242", amount="Per 100 grams",
                       ftype="Meat", food=food)

session.add(foodChart25)
session.commit()


print "All the food items are added!"
