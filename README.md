# CarChecker
Heroku: https://intense-ravine-02428.herokuapp.com

Functionalities

POST /cars
* Request body contain car make (key = "make") and model name (key = "model")
* Based on this data, its existence ischecked here https://vpic.nhtsa.dot.gov/api/ (in case of https://vpic.nhtsa.dot.gov/api/ is unavailable you will receive appropriate information)
* If the car doesn't exist - return an error
* If the car exists - it should be saved in the database

POST /rate
* Add a rate for a car from 1 to 5
* Request body contain car PrimaryKey (key = "car") and rate (key = "rate")
GET /cars
* Should fetch list of all cars already present in application database with their current average rate an number of rates
GET /popular
* Should return top cars already present in the database ranking based on number of rates (not average rate values, it's important!)

SETUP:
requirements:
*Docker, docker-compose

* clone this repository to an empty directory
* open your console and type "docker-compose build web"
* after it is built type "docker-compose up" - Now CarChecker is running locally

TEST:
* open new console tab and type "docker-compose exec web ash", then "python manage.py test"
* Wait for the tests to be performed. Sometimes https://vpic.nhtsa.dot.gov/api/ is undergoing Maintenance, then some tests will be failed (as they should!) 
