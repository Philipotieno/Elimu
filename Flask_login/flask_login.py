from flask import Flask, session
import flask_login

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/login")
def login():
	session['User'] = "Anthony"
	return 'Index'

@app.route("/getsession")
def getsession():
	if 'user' in session:
		return session['user']

	return 'Is Not logged in! '

@app.route("/dropsession")
def dropsession():
	session.pop("user", None)
	return 'Dropped!'

	
if (__name__ == "__main__"):
    app.run(debug=True)
