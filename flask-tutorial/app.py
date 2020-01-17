from flask import Flask, session, render_template, request, url_for, redirect
from scripts import query

app = Flask(__name__)


app.secret_key = 'secret_key'


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/signin', methods=['POST', 'GET'])
def signin():
	if request.method == 'POST':
		if query.signin(request.form) == "success":
			session['logged_in'] = True
			session['username'] = request.form['username']
		else:
			session['logged_in'] = False
		return render_template('main.html')
	else:
		return render_template('signin.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if request.method == 'POST':
		a = query.signup(request.form)
		if a == "success":
			print (a)
		elif a == "duplicated":
			print (a)
		else:
			print (a)
		return render_template('main.html')
	else:
		return render_template('signup.html')


@app.route('/signout')
def signout():
	session['logged_in'] = False
	session['username'] = ""
	return render_template('main.html')


@app.route('/info', methods=['POST','GET'])
def info():
	r = query.get_data(session['username'])
	return render_template('info.html', username=r['username'], password=r['password'], email=r['email'])


@app.route('/programs')
def programs():
	return render_template('programs.html')


@app.route('/base')
def base():
	return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)