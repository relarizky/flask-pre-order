# Flask-Pre-Order

![https://img.shields.io/github/license/relarizky/flask-pre-order](https://img.shields.io/github/license/relarizky/flask-pre-order)
![https://travis-ci.com/relarizky/flask-pre-order.svg?branch=master](https://travis-ci.com/relarizky/flask-pre-order.svg?branch=master)
![https://img.shields.io/badge/python-3.9-brightgreen](https://img.shields.io/badge/python-3.9-brightgreen)

<img src='https://raw.githubusercontent.com/relarizky/flask-pre-order/master/screenshot/1.png' 
          width=20% height=15%> <img src='https://raw.githubusercontent.com/relarizky/flask-pre-order/master/screenshot/2.png' 
          width=20% height=15%> <img src='https://raw.githubusercontent.com/relarizky/flask-pre-order/master/screenshot/3.png' 
          width=20% height=15%> <img src='https://raw.githubusercontent.com/relarizky/flask-pre-order/master/screenshot/4.png' 
          width=20% height=15%>

<img src='https://raw.githubusercontent.com/relarizky/flask-pre-order/master/screenshot/5.png' 
          width=20% height=15%> <img src='https://raw.githubusercontent.com/relarizky/flask-pre-order/master/screenshot/6.png' 
          width=20% height=15%> <img src='https://raw.githubusercontent.com/relarizky/flask-pre-order/master/screenshot/7.png' 
          width=20% height=15%>


## Features

  - Multiple User with different login page
  - Email Confirmation and Notification
  - Generate PDF as report
          

## Installation

### MySQL 
```
$ git clone https://github.com/relarizky/flask-pre-order.git
$ cd flask-pre-order
$ pip install -r requirements.txt
$ export SECRET_KEY=<random str>
$ export FLASK_DBMS=MySQL
$ export HOST_NAME=<db hostname>
$ export USER_NAME=<db username>
$ export PASS_WORD=<db password>
$ export DATA_BASE=<db name>
$ export MAIL_USERNAME=<your gmail email>
$ export MAIL_PASSWORD=<your gmail password>
$ export JWT_SECRET_KEY=<random str>
$ flask db init; flask db migrate; flask db upgrade
$ python seeder.py
$ python run.py
```

### SQLite
```
$ git clone https://github.com/relarizky/flask-pre-order.git
$ cd flask-pre-order
$ pip install -r requirements.txt
$ export SECRET_KEY=<random str>
$ export FLASK_DBMS=SQLite
$ export FILE_NAME=<database file name>
$ export MAIL_USERNAME=<your gmail email>
$ export MAIL_PASSWORD=<your gmail password>
$ export JWT_SECRET_KEY=<random str>
$ flask db init; flask db migrate; flask db upgrade
$ python seeder.py
$ python run.py
```

All you have to do with your gmail account for using this app is, allow your account to be accessed/used from unsecured apps.

After successfully install the app, you can login into dashboard with these default admin:

  - admin:12345678
  - testadmin:12345678
  
And the admin login page is [http://localhost:5000/auth/admin](http://localhost:5000/auth/admin)


## Demo

For demo, visit this link [https://flask-pre-order.herokuapp.com/](https://flask-pre-order.herokuapp.com/)
