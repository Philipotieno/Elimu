from flask import *
from flask import Flask
import jwt
from flask_jwt import JWT
import datetime
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisandela'

def required(fn):
    @wraps(fn)
    def decorator(*args,**kwargs):
        
        if request.args.get('token')=='':
            return jsonify({"Message":'Please log in'})
        try:
            jwt.decode(request.args.get('token'), app.config['SECRET_KEY'])
        except:
            return jsonify({"Message":'You are not logged in'})
        return fn(*args,**kwargs)
    return decorator


details = {}
comments = []

@app.route('/', methods=['POST', 'GET'])
def index():
 	return jsonify({"Message": "Hello Welcome!"})

@app.route('/register', methods=['POST', 'GET'])
def register():
	data = request.get_json()
	Name = data['Name']
	Email = data['Email']
	Username = data['Username']
	Password = data['Password']
	details.update({"Name": Name, "Email": Email, "Username" : Username, "Password": Password})

	return jsonify({"Message": "Registration successfull"})

	return jsonify({"Homepage": "Hello Welcome to my homepage"})

@app.route("/login",methods=["GET","POST"])
def login():
	data = request.get_json()
	Username = data['Username']
	Password = data['Password']
	if Username==details["Username"]:
		if Password==details["Password"]:
			token = jwt.encode({"Username":Username,"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=1)},app.config['SECRET_KEY'])
			return jsonify({"token":token.decode('utf-8')})
		else:
			return jsonify({"Message": "Wrong password, try again later"})
	else:
		return jsonify({"Message": "Please provide the right username"})

@app.route("/comment",methods=["GET","POST"])
def comment():
    data=request.get_json()
    comment = data['comment']
    comments.append(comment)
    return jsonify({"Message": "Comment sent"})


@app.route("/view_comment",methods=["GET"])
def view_comments():
    view={}
    for each in comments:
        view.update({comments.index(each):each})
    return jsonify(view)

@app.route("/user_details",methods=["GET"])   
def user_details():
    return jsonify(details)


@app.route('/remove_details/<int:commentID>', methods=['DELETE'])
def remove_details(commentID):
	del comments[commentID]
	return jsonify({"Info": "You have deleted a comment"})


if __name__ == '__main__':
    app.run(debug=True, port=7556)


'''

{
	"Name":"Philip", 
	"Email":"emailemail@gmail.com",
	"Username": "otibmt",
	"Password": "password"
	
}


{
	"Username": "otibmt",
	"Password": "password"
}


{
	"comment": "my name is philip",
	"comment": "my other name is otieno",
	"comment": "jesus is Lord",
	"comment": "this is andela"
}

'''
