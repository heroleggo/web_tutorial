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
			email = query.get_data(request.form['username'])['email']
			session['email'] = email
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
	session['email'] = ""
	return render_template('main.html')


@app.route('/info', methods=['POST','GET'])
def info():
	r = query.get_data(session['username'])
	if request.method == 'POST':
		data = {'username':request.form['up_username'], 'password':request.form['up_password'], 'email':session['email']}
		q1 = query.update(data)
		q2 = query.get_data(request.form['up_username'])
		return render_template('info.html', username=q2['username'], password=q2['password'], email=q2['email'])
	else:
		return render_template('info.html', username=r['username'], password=r['password'], email=r['email'])


@app.route('/programs')
def programs():
	return render_template('programs.html')


@app.route('/base')
def base():
	return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)