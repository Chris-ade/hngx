class Person(db.Model):
    ''' This is a model that initialize a table titled `person` with columns id, name, email, gender and age.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Person {self.name}>'
