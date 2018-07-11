# Database Intergration with  JWT Authorization in Flask
 --A flask-restful application where users can register, login, create comment, edit comment, delete his/her comment and view all comments and who posted the comments.

 -the user details and comments are stored in an sqlite db

## How to run

``` bash
clone this branch  --- https://github.com/Philipotieno/Elimu.git

cd into the Challemge_ten 

virtualenv -p python3 venv

source venv/bin/activate


pip install flask flask-restful flask-jwt-extended passlib flask-sqlalchemy

pip install -r requirements.txt

run.py file to start the server
	
use postman to view the outputs of differenten views
# localhost:5000
	/registration : to register users
	/login        :Log in registered users
	/comment      :post comments   
	/view         :view comments posted
	/user         :View registered users

```