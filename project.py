from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Food, FoodChart, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Nutrition"


# Connect to Database and create database session
engine = create_engine('sqlite:///nutritioncontentwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img class="login-pic" src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    print "Credentials: ", credentials
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON APIs to view Nutrition content of the food
@app.route('/food/<int:food_id>/list/JSON')
def foodlistJSON(food_id):
    food = session.query(Food).filter_by(id=food_id).one()
    items = session.query(FoodChart).filter_by(
        food_id=food_id).all()
    return jsonify(FoodChart=[i.serialize for i in items])


@app.route('/food/<int:food_id>/foodchart/<int:foodchart_id>/JSON')
def foodChartJSON(food_id, foodchart_id):
    Food_Chart = session.query(FoodChart).filter_by(id=foodchart_id).one()
    return jsonify(Food_Chart=Food_Chart.serialize)


@app.route('/food/JSON')
def foodsJSON():
    foods = session.query(Food).all()
    return jsonify(foods=[r.serialize for r in foods])


# Show all foods
@app.route('/')
@app.route('/food/')
def showFoods():
    foods = session.query(Food).order_by(asc(Food.name))
    if 'username' not in login_session:
        return render_template('publicfoods.html', foods=foods)
    else:
        return render_template('foods.html', foods=foods)


# Add a new food
@app.route('/food/new/', methods=['GET', 'POST'])
def newFood():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newFood = Food(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newFood)
        flash('New Food %s Successfully Created' % newFood.name)
        session.commit()
        return redirect(url_for('showFoods'))
    else:
        return render_template('newFood.html')


# Edit a food
@app.route('/food/<int:food_id>/edit/', methods=['GET', 'POST'])
def editFood(food_id):
    editedFood = session.query(
        Food).filter_by(id=food_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedFood.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this Food. Please create your own food in order to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedFood.name = request.form['name']
            flash('Food Successfully Edited %s' % editedFood.name)
            return redirect(url_for('showFoods'))
    else:
        return render_template('editFood.html', food=editedFood)


# Delete a food
@app.route('/food/<int:food_id>/delete/', methods=['GET', 'POST'])
def deleteFood(food_id):
    foodToDelete = session.query(
        Food).filter_by(id=food_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if foodToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this food. Please create your own food in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(foodToDelete)
        flash('%s Successfully Deleted' % foodToDelete.name)
        session.commit()
        return redirect(url_for('showFoods', food_id=food_id))
    else:
        return render_template('deleteFood.html', food=foodToDelete)


# Show a food list
@app.route('/food/<int:food_id>/')
@app.route('/food/<int:food_id>/foodchart/')
def showFoodChart(food_id):
    food = session.query(Food).filter_by(id=food_id).one()
    creator = getUserInfo(food.user_id)
    items = session.query(FoodChart).filter_by(
        food_id=food_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicfoodchart.html', items=items, food=food, creator=creator)
    else:
        return render_template('foodchart.html', items=items, food=food, creator=creator)


# Create a new Food Chart
@app.route('/food/<int:food_id>/foodchart/new/', methods=['GET', 'POST'])
def newFoodChart(food_id):
    if 'username' not in login_session:
        return redirect('/login')
    food = session.query(Food).filter_by(id=food_id).one()
    if login_session['user_id'] != food.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add food items to food chart. Please add your own food in order to add items.');}</script><body onload='myFunction()''>"
        if request.method == 'POST':
            newItem = FoodChart(name=request.form['name'], protein=request.form['protein'], carbs=request.form[
                               'carbs'], fats=request.form['fats'], calories=request.form['calories'],
                               amount=request.form['amount'], food_id=food_id, user_id=food.user_id)
            session.add(newItem)
            session.commit()
            flash('New Food %s Item Successfully Created' % (newItem.name))
            return redirect(url_for('showFoodChart', food_id=food_id))
    else:
        return render_template('newfoodchart.html', food_id=food_id)


# Edit a Food Chart
@app.route('/food/<int:food_id>/foodchart/<int:foodchart_id>/edit', methods=['GET', 'POST'])
def editFoodChart(food_id, foodchart_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = session.query(FoodChart).filter_by(id=foodchart_id).one()
    restaurant = session.query(Food).filter_by(id=food_id).one()
    if login_session['user_id'] != food.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit food items to food chart. Please create your own food in order to edit items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['protein']:
            editedItem.protein = request.form['protein']
        if request.form['carbs']:
            editedItem.carbs = request.form['carbs']
        if request.form['fats']:
            editedItem.fats = request.form['fats']
        if request.form['calories']:
            editedItem.calories = request.form['calories']
        if request.form['amount']:
            editedItem.amount = request.form['amount']
        session.add(editedItem)
        session.commit()
        flash('Food Item Successfully Edited')
        return redirect(url_for('showFoodChart', food_id=food_id))
    else:
        return render_template('editfoodchart.html', food_id=restaurant_id, foodchart_id=menu_id, item=editedItem)


# Delete a Food Item
@app.route('/food/<int:food_id>/menu/<int:foodchart_id>/delete', methods=['GET', 'POST'])
def deleteFoodChart(food_id, foodchart_id):
    if 'username' not in login_session:
        return redirect('/login')
    food = session.query(Food).filter_by(id=food_id).one()
    itemToDelete = session.query(FoodChart).filter_by(id=foodchart_id).one()
    if login_session['user_id'] != food.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete food items from food chart. Please create your own food chart in order to delete items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Food Item Successfully Deleted')
        return redirect(url_for('showFoodchart', food_id=food_id))
    else:
        return render_template('deleteFoodChart.html', item=itemToDelete)


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['credentials']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showFoods'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showFoods'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
