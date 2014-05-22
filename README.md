'''
RESTful APIs
How to make a RESTful API from scratch in Python using the Python Flask Framework using
Ubuntu Linux OS which as a bonus handles geosptatial data.
'''

RESTful API's are stateless,meaning everything the server needs to process the request
is sent at the same time in the same transaction.

Prerequisites:
1.Your database of choice is installed. MySQL in this example. (sudo apt-get install mysql-server mysql-client)
2.Python is installed.
Note: Install and activate a virtualenv to work out of for the rest of these below: 
3.Flask is installed. (from bash prompt $ pip install flask) 
4.Flask sql alchemy is installed.  (from bash prompt $pip install flask-sqlalchemy)
5.MySQLdb is installed. (from bash prompt $pip install mysql-python)



Overview of this guide:
1.Get the data you want your API to interact with. (Parse via XML/JSON/CSV)
2.Enter that data into a database. (MySQL,MongoDB...)
3.Design your RESTful API
4.Implement your API



1. Get some data: 
We're going to invent some data here but normally you'd get data from parsing it on the web
from whatever format it comes in to a text file. 

2. ETL your data into your database of choice(We're using MySQL today):
Login to MySQL from bash prompt infile=1$: 
mysql --local-infile=1 -u username -p

Then run the following commands in your mysql prompt (will display as 'mysql>' in bash).
mysql>CREATE DATABASE mikesmotorshops;
mysql>USE mikesmotorshops;
mysql>CREATE TABLE motorshops (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    store_number INT(8),
    number_of_employees INT(8),
    location VARCHAR(100),
    speciality VARCHAR(20),
    average_turnaround VARCHAR(10),
    description TEXT,
    lat FLOAT(10, 6),
    lng FLOAT(10, 6)
  ) ENGINE = MYISAM CHARACTER SET utf8 COLLATE utf8_general_ci;

mysql> LOAD DATA LOCAL INFILE '/path/mikesmotorshops.tsv' INTO TABLE mikesmotorshops 
FIELDS TERMINATED BY '\t' ENCLOSED BY '"' LINES TERMINATED BY '\n';

Great now your data is in your database and we can create your own RESTful API.

3.Designing a RESTful API:

Note:We will follow the REST guidelines for creating our RESTful API's. 
Namely URLs should only identify resources and HTTP verbs should derive from 
actions on those resources.

Note:Two URLs are needed per resource so you can interact with the collection as 
a whole and a singular item of that collection. 

Lets use a fictitious chain of motorshops called Mike's Motors:
```html
Example:
For a collection of motor shops in the USA:
 A. For the data collection : /motorshops/
 B. For a specific instance(row/element) of that collection: /motorshops/<id>
```

Let's map out what we want to happen with each "verb" request. (POST,GET,DELETE and PUT)

POST /motorshops/   (GOOD: add a new motorshop)
POST /motorshops/<id> (ERROR: add a new motorshop to id.)

GET /motorshops/   (GOOD: return a list of all motorshops)
GET /motorshops/<id> (GOOD: return a list of a motorshop with that id.)

PUT /motorshops/   (GOOD: update all motorshops)
PUT /motorshops/<id> (GOOD: add a new motorshop to id.)

DELETE /motorshops/   (GOOD: delete all motorshops)
DELETE /motorshops/<id> (GOOD: delete a motorshop with that id.)


4.Implementing the RESTful API.
Now let's check out route.py.
Note: '#' denote what each section of the code does as soon as we encounter it.









