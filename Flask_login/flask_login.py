from flask import Flask, session, render_template, request,redirect, g, url_for

app = Flask(__name__)
app.secret_key = "philip"

@app.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		session.pop('user', None)

		if request.form['password'] == 'password':
			session['user'] = request.form['username']
			return redirect(url_for('post'))

	return render_template('index.html')


@app.route('/post')
def post():
	if g.user:
		return render_template('post.html')

	return redirect(url_for('index'))



@app.route('/login')
def login():
	if 'user' in session:
		return redirect(url_for('index'))
	else:
		return 'Not logged in!'

@app.route('/logout')
def logout():
	session.pop('user')

	return "<h2>Logged out</h2>"



if __name__ == '__main__':
	app.run(debug=True, port=5070)