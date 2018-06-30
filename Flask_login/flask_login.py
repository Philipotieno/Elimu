from flask import Flask, session, render_template, request,redirect, g, url_for

app = Flask(__name__)
app.secret_key = "philip"


#main route
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		session.pop('username',None)

		if request.form['password'] == 'password':
			session['username'] = request.form['username']
			return redirect(url_for('post'))

	return render_template('index.html')

@app.route('/post')
def post():
	if g.user:
		return render_template('post.html')
	else:
		return redirect(url_for('index'))


@app.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['username']

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		return session['username']
	else:
		return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	return '<h2>You are logged out</h2>'


if __name__ == '__main__':
	app.run(debug=True, port=5045)