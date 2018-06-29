from flask import Flask, session, render_template, request,redirect, g, url_for

app = Flask(__name__)
app.secret_key = "philip"

users = { }

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		session.pop('user',None)

		if request.form['password'] == 'password':
			session['user'] = request.form['username']
			return redirect(url_for('post'))

	return render_template('index.html')

@app.route('/post')
def post():
	if g.user:
		return render_template('post.html')

	return redirect(url_for('index'))


@app.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']

@app.route('/login')
def login():
	if 'user' in session:
		return session['user']
	else:
		return 'Not logged in'

@app.route('/logout')
def logout():
	session.pop('user', None)
	return '<logged out>'


if __name__ == '__main__':
	app.run(debug=True, port=5033)