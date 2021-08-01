<h1 align='center'>
  Hi there 👋 I'm Abhishek 👨‍💻
</h1>

<p align='center'>
  This is the assignment submitted by me for Krypto Django Developer Role.
</p>



<p align='center'>
  
  <a href="https://www.linkedin.com/in/1nonlyabhi/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>&nbsp;&nbsp;
  <a href="https://twitter.com/1nonlyabhi">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" />        
  </a>&nbsp;&nbsp;
  
</p>


## Setup

1. Git Clone the project with: ```git clone https://github.com/1nonlyabhi/krypto-assignment```.

2. Move to the base directory: ```cd krypto-assignment```

3. Create a new python enveronment with: ```python -m venv krypto-env```.

4. Activate enveronment with: ```env\Scripts\activate``` on windows, or ```source env/bin/activate``` on Mac and Linux.

5. Install required dependences with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

7. Run app localy with: ```python manage.py runserver```.

8. Run python-script to test in other terminal with: ```python manage.py test```.

9. Download postman from: ```https://www.postman.com/downloads/```.


## Problem Statement 
[Problem Statement Django Role](https://docs.google.com/document/d/1QbtOghwUI2AvScamlyphnNRvueFuwllu8EGJoHoofds/edit "Click here to see the problem statement")


## Requests

#### Register the user

`POST /users/register`

    {
        "username": "username",
        "email": "emailaddress@gmail.com",
        "password": "password"
    }

#### Generate the access token

`POST /api/token/`

    {
        "username": "username",
        "email": "emailaddress@gmail.com",
    }

### Alert Model

| Column      | Type     | Default |
| ----------- | -------- | ------- |
| targetPrice | Integer  |	       |
| created     | Boolean  | False   |
| deleted     | Boolean  | False   |
| triggered   | Boolean  | False   |
| holder      | User     |	       |


#### To create an alert

`POST /alerts/manage`

    {
        "targetPrice": 33000
    }

#### To update an alert

`POST /alerts/manage`

    {
        "id": 1,
        "targetPrice": 33000,
        "created": true,
        "deleted": false,
    }

#### To modify an alert

`PATCH /alerts/manage`

    {
        "id": 1,
        "targetPrice": 43000,
    }

#### To delete an alert

`DELETE /alerts/manage`

    {
        "id": 1,
    }

* _You can just update the flag from ```False``` to ```True``` through the ```PATCH``` request which will not delete the record from database but if you send the ```DELETE``` request, it'll get deleted permanently._


#### To get the list of alerts created by that user & filter the alerts on tha basis of status

* `GET /alerts/alertlist`

* `GET /alerts/alertlist?status=triggered`


#### To modify an alert

`POST /alerts/currentprice`

    {
         "currentPrice": 29000
    }

#### Run the python-script

To run the python-script which is written in the ```alerts/test.py``` file, open another terminal and run the command: ```python manage.py test```
_This test will run after every 10 seconds on the basis of random generated integer number which set the current price of BTC._
* In order to use real-time BTC price's API, we just have to get the currentprice of BTC and pass it to the number variable. Also some basic changes will be needed.


* Note: _This repo also has a branch named ```Version 1.0``` which is a basic solution to the problem statement._
