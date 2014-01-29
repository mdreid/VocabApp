

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(20), unique = True)
	email = db.Column(db.String(50), unique = True)
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	words = db.relationship('Word', backref = 'user', lazy = 'dynamic')

	def __repr__(self):
		return 'User: %r' % (self.nickname)

class Word(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	wd = db.Column(db.String(30))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	sentences = db.relationship('Sentence', backref = 'word', lazy = 'dynamic')

	def __repr__(self):
		return 'Word: %r' % (self.wd)

class Sentence(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(500))
	citation = db.Column(db.String(100), default = 'None')
	timestamp = db.Column(db.DateTime)
	word_id = db.Column(db.Integer, db.ForeignKey('word.id'))

	def __repr__(self):
		return 'Sentence: %r' % (self.body)