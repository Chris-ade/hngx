class Person(db.Model):
    ''' This is a model that initialize a table titled `person` with columns id, name, email, gender and age.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    gender = db.Column(db.String(6))
    age = db.Column(db.Integer)