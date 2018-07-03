from flask import *

app = Flask(__name__)

app.config['SECTRET_KEY'] = 'thisisandela'

details = {}
comments = []

@app.route('/', methods=['POST', 'GET'])
def index():
	return jsonify({"Homepage": "Hello Welcome to my homepage"})

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
	if Username in details:
		if Password=="Password":
			session["logged_in"]=True
			return jsonify({"Message": "Login successful"})
		else:
			return jsonify({"Message": "Wrong password, try again later"})
	else:
		return jsonify({"Message": "Please provide the right username"})

@app.route("/comment",methods=["GET","POST"])
def comment():
    data=request.get_json()["comment"]
    comment = data["comment"]
    store_comments.append(comment)
    return jsonify({"Message": "Comment sent"})


@app.route("/view_comment",methods=["GET"])
def view_comments():
    output={}
    for each in store_comments:
        output.update({store_comments.index(each):each})
    return jsonify(output)

@app.route("/user_details",methods=["GET"])   
def user_details():
    return jsonify(details)

if __name__ == '__main__':
    app.run(debug=True, port=9956)


'''

{
	"Name":"Philip", 
	"Email":"emailemail@gmail.com",
	"Username": "otibmt",
	"Password": "password"
	
}

'''