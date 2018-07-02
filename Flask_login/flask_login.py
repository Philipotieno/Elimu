 #!/usr/bin/env python
'''
Flask app where logged in users can:
comment up
fetch details
fetch comments
view user details
'''
from flask import Flask, session, render_template, request, redirect, g, url_for

app = Flask(__name__) # pylint: disable=invalid-name
app.secret_key = "philip"

@app.before_request  # pylint: disable=invalid-name
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/', methods=['GET', 'POST'])  # pylint: disable=invalid-name
def index():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('post'))

    return render_template('index.html')


@app.route('/post') # pylint: disable=invalid-name
def post():
    if g.user:
        return render_template('post.html')

    return redirect(url_for('index'))

@app.route('/comment') # pylint: disable=invalid-name
def comment():
    if g.user:
        return render_template('comment.html')

    return redirect(url_for('index'))

@app.route('/details', methods=['GET', 'POST']) # pylint: disable=invalid-name
def details():
    if 'user' in session:
        text = request.form['name']
        processed_text = text.upper()
        return processed_text

    return render_template('index.html')


@app.route('/login') # pylint: disable=invalid-name
def login():
    if 'user' in session:
        return redirect(url_for('post'))

    return render_template('index.html')

@app.route('/logout') # pylint: disable=invalid-name
def logout(): #user can log out
    session.pop('user')
    return "<h2>Logged out</h2>"



if __name__ == '__main__':
    app.run(debug=True, port=5054)
