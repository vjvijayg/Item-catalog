from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Food, Base, FoodChart, User

engine = create_engine('sqlite:///nutritioncontentwithusers.db')
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
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture="https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png")
session.add(User1)
session.commit()

# Fruits list with nutional content
food1 = Food(user_id=1, name="foodcat1")

session.add(food1)
session.commit()


foodChart1 = FoodChart(user_id=1, name="Bananas", protein="1.1g", carbs="23g",
                       fats="0.3g", calories="89", amount="Per 100 grams",
                       ftype="Fruits", food=food1)

session.add(foodChart1)
session.commit()


foodChart2 = FoodChart(user_id=1, name="Apples", protein="0.3g", carbs="14g",
                       fats="0.2g", calories="52", amount="Per 100 grams",
                       ftype="Fruits", food=food1)

session.add(foodChart2)
session.commit()


foodChart3 = FoodChart(user_id=1, name="Oranges", protein="0.9g", carbs="12g",
                       fats="0.1g", calories="47", amount="Per 100 grams",
                       ftype="Fruits", food=food1)

session.add(foodChart3)
session.commit()


foodChart4 = FoodChart(user_id=1, name="Pomegranates", protein="1.7g", carbs="19g",
                       fats="1.2g", calories="83", amount="Per 100 grams",
                       ftype="Fruits", food=food1)

session.add(foodChart4)
session.commit()


# Root Vegetables list with nutional content
food2 = Food(user_id=1, name="foodcat2")

session.add(food2)
session.commit()


foodChart1 = FoodChart(user_id=1, name="Potatoes", protein="2g", carbs="17g",
                       fats="0.1g", calories="77", amount="Per 100 grams",
                       ftype="Root Vegetables", food=food2)

session.add(foodChart1)
session.commit()


foodChart2 = FoodChart(user_id=1, name="Carrots", protein="0.9g", carbs="10g",
                       fats="0.2g", calories="41", amount="Per 100 grams",
                       ftype="Root Vegetables", food=food2)

session.add(foodChart2)
session.commit()


foodChart3 = FoodChart(user_id=1, name="Raddishes", protein="0.7g", carbs="3.4g",
                       fats="0.1g", calories="16", amount="Per 100 grams",
                       ftype="Root Vegetables", food=food2)

session.add(foodChart3)
session.commit()


foodChart4 = FoodChart(user_id=1, name="Beetroots", protein="1.6g", carbs="10g",
                       fats="0.2g", calories="43", amount="Per 100 grams",
                       ftype="Root Vegetables", food=food2)

session.add(foodChart4)
session.commit()


# Vegetables list with nutional content
food3 = Food(user_id=1, name="foodcat3")

session.add(food3)
session.commit()


foodChart1 = FoodChart(user_id=1, name="Tomatoes", protein="0.9g", carbs="3.9g",
                       fats="0.2g", calories="18", amount="Per 100 grams",
                       ftype="Vegetables", food=food3)

session.add(foodChart1)
session.commit()


foodChart2 = FoodChart(user_id=1, name="Brinjal", protein="1g", carbs="6g",
                       fats="0.2g", calories="25", amount="Per 100 grams",
                       ftype="Vegetables", food=food3)

session.add(foodChart2)
session.commit()


foodChart3 = FoodChart(user_id=1, name="Ladies fingers", protein="1.9g", carbs="7g",
                       fats="0.2g", calories="33", amount="Per 100 grams",
                       ftype="Vegetables", food=food3)

session.add(foodChart3)
session.commit()


foodChart4 = FoodChart(user_id=1, name="Broccoli", protein="2.8g", carbs="7g",
                       fats="0.4g", calories="34", amount="Per 100 grams",
                       ftype="Vegetables", food=food3)

session.add(foodChart4)
session.commit()


foodChart5 = FoodChart(user_id=1, name="Mushrooms", protein="3.1g", carbs="3.3g",
                       fats="0.3g", calories="22", amount="Per 100 grams",
                       ftype="Vegetables", food=food3)

session.add(foodChart5)
session.commit()


# Leaf Vegetables list with nutional content
food4 = Food(user_id=1, name="foodcat4")

session.add(food4)
session.commit()


foodChart1 = FoodChart(user_id=1, name="Spinach", protein="2.9g", carbs="3.6g",
                       fats="0.4g", calories="23", amount="Per 100 grams",
                       ftype="Leaf Vegetables", food=food4)

session.add(foodChart1)
session.commit()


foodChart2 = FoodChart(user_id=1, name="Kale", protein="4.3g", carbs="9g",
                       fats="0.9g", calories="49", amount="Per 100 grams",
                       ftype="Leaf Vegetables", food=food4)

session.add(foodChart2)
session.commit()


foodChart3 = FoodChart(user_id=1, name="Mustard Greens", protein="2.9g", carbs="4.7g",
                       fats="0.4g", calories="27", amount="Per 100 grams",
                       ftype="Leaf Vegetables", food=food4)

session.add(foodChart3)
session.commit()


foodChart4 = FoodChart(user_id=1, name="Chard", protein="1.8g", carbs="3self.7g",
                       fats="0.2g", calories="19", amount="Per 100 grams",
                       ftype="Leaf Vegetables", food=food4)

session.add(foodChart4)
session.commit()


# Lentils list with nutional content
food5 = Food(user_id=1, name="foodcat5")

session.add(food5)
session.commit()


foodChart1 = FoodChart(user_id=1, name="Mung Beans", protein="24g", carbs="63g",
                       fats="1.2g", calories="347", amount="Per 100 grams",
                       ftype="Lentils", food=food5)

session.add(foodChart1)
session.commit()


foodChart2 = FoodChart(user_id=1, name="Kidney Beans", protein="24g", carbs="60g",
                       fats="0.8g", calories="333", amount="Per 100 grams",
                       ftype="Lentils", food=food5)

session.add(foodChart2)
session.commit()


foodChart3 = FoodChart(user_id=1, name="Pigeon Peas", protein="22g", carbs="63g",
                       fats="1.5g", calories="343", amount="Per 100 grams",
                       ftype="Lentils", food=food5)

session.add(foodChart3)
session.commit()


foodChart4 = FoodChart(user_id=1, name="Soya Bean", protein="36g", carbs="30g",
                       fats="20g", calories="446", amount="Per 100 grams",
                       ftype="Lentils", food=food5)

session.add(foodChart4)
session.commit()


# Meat list with nutional content
food6 = Food(user_id=1, name="foodcat6")

session.add(food6)
session.commit()


foodChart1 = FoodChart(user_id=1, name="Chicken", protein="31g", carbs="0g",
                       fats="3.6g", calories="167", amount="Per 100 grams",
                       ftype="Meat", food=food6)

session.add(foodChart1)
session.commit()


foodChart2 = FoodChart(user_id=1, name="Mutton", protein="25g", carbs="0g",
                       fats="21g", calories="294", amount="Per 100 grams",
                       ftype="Meat", food=food6)

session.add(foodChart2)
session.commit()


foodChart3 = FoodChart(user_id=1, name="Fish", protein="22g", carbs="0g",
                       fats="12g", calories="206", amount="Per 100 grams",
                       ftype="Meat", food=food6)

session.add(foodChart3)
session.commit()


foodChart4 = FoodChart(user_id=1, name="Pork", protein="27g", carbs="0g",
                       fats="14g", calories="242", amount="Per 100 grams",
                       ftype="Meat", food=food6)

session.add(foodChart4)
session.commit()


print "All the food items are added!"
