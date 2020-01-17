from . import db

def signup(data):
	dbs = db.database()
	em = data['email']
	un = data['username']
	pw = data['password']
	sq = "SELECT * FROM info WHERE `username`=%s"
	r = dbs.executeOne(sq, un)
	if r:
		return "duplicated"
	else:
		sq2 = "INSERT INTO info(username, password, email) VALUES('%s','%s','%s')" % (un, pw, em)
		r2 = dbs.executeOne(sq2)
		if r2:
			dbs.commit()
			return "success"
		else:
			return "fail"


def signin(data):
	dbs = db.database()
	un = data['username']
	pw = data['password']
	sq = "SELECT * FROM info WHERE `username`='%s' and `password`='%s'" % (un, pw)
	r = dbs.executeOne(sq)
	if r:
		return "success"
	else:
		return "fail"


def get_data(username):
	print (username)
	dbs = db.database()
	sq = "SELECT * FROM info WHERE `username`='%s'" % (username)
	r = dbs.executeOne(sq)
	return r