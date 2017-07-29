# Item-catalog

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as 
provide a user registration and authentication system. It is an application built in python for the Udacity Full Stack Nanodegree. It focuses on building SQL queries, datatables, and proper code formating.

Files you will need are:
* database_setup.py
* lotsofparks.py
* project.py

## How to use
You will need to have Python and Vagrant to run on a VM.
You will also need to clone this repo, you can do so by doing the following:
```
$ git clone https://github.com/cgraffeo/Item-catalog
```
Now you will need to CD into the apropriate files, create a database by running database_setup.py:
```
-> vagrant ssh
$ cd /vagrant
$ cd item-catalog/
$ python  database_setup.py
$ python lotsofparks.py
```
The program has been built to create a databse and populate it with all of the states for you.

Run the project file:
```
$python project.py
```

## Project will now be available on localhost:8000
