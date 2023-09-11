import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# SQLite database initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'persons.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    ''' This is a model that initialize a table titled `person` with columns id, name, email, gender and age.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    gender = db.Column(db.String(6), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Person {self.name}>'

@app.route('/api', methods=['POST'])
def create_person():
    ''' This endpoint takes a POST request to create a person and store it in the database.
    
    Parameters:
        name (str): A key passed as a JSON payload of the POST request which value indicates the name of the person being created.
        
        email (str): A key passed as a JSON payload of the POST request which value indicates the email address of the person being created.
        
        gender (str): A key passed as a JSON payload of the POST request which value indicates the gender of the person being created.
        
        age (int): A key passed as a JSON payload of the POST request which value indicates the age of the person being created.

    Returns:
        JSON: A json response returns a message indicating if the task was successful or an error message.

    Example:
        POST /api/ {'name': 'Chris', 'email': 'chris@hngx.com', 'gender': 'male', 'age': 21}
    '''
    try:
        # Loads the request body
        data = request.get_json()
        name = data['name']
        email = data['email']
        gender = data['gender']
        age = int(data['age'])
        
        # Input validation
        if not isinstance(name, str) or not isinstance(age, int) or not isinstance(email, str) or not isinstance(age, int):
            return jsonify({'error': 'Invalid input data'}), 400
        
        person = Person.query.filter_by(name=name, email=email).first()

        if person:
            return jsonify({'message': 'A person with this name and email address already exists'}), 400
        else:
            person = Person(name=name, email=email, gender=gender, age=age)
            db.session.add(person)
            db.session.commit()

            # Returns a message in Json
            return jsonify({'message': 'Person created successfully', 'id': person.id}), 201
    
    # Handles empty or invalid keys
    except (KeyError, ValueError):
        db.session.rollback()
        return jsonify({'error': "Invalid request"}), 400

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    ''' This endpoint takes a GET request to fetch a specific person in the database.
    
    Parameters:
        user_id (int): A parameter passed in the URL which value indicates the person's ID and data to fetch.

    Returns:
        JSON: A json response returns a message indicating if the task was successful or an error message.

    Example:
        GET /api/<user_id>
    '''
    try:
        # Input validation
        if not isinstance(user_id, int):
            return jsonify({'error': 'Invalid input data'}), 400
            
        person = Person.query.filter_by(id=user_id).first()

        if person:
            person_data = {
                'id': person.id,
                'name': person.name,
                'email': person.email,
                'gender': person.gender,
                'age': person.age
            }
            return jsonify({'person': person_data}), 200
        else:
            return jsonify({'message': 'Person not found or does not exist'}), 404

    # Returns an error if the request body key or value is absent
    except (KeyError, ValueError):
        return jsonify({'error': "Invalid request"}), 400

@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    ''' This endpoint takes a PUT request to update a specific person gender in the database.
    
    Parameters:
        user_id (int): A parameter passed in the URL which value indicates the ID of the person to update.
        
        age (int): A key passed as a JSON payload of the PUT request which value indicates the new value for the person's age.
        
    Returns:
        JSON: A json response returns a message indicating if the task was successful or an error message.

    Example:
        PUT /api/<user_id> {'age': 21}
    '''
    try:
        # Loads the request body
        data = request.get_json()
        age = int(data['age'])

        # Input validation
        if not isinstance(user_id, int) or not isinstance(age, int):
            return jsonify({'error': 'Invalid input data'}), 400

        person = Person.query.filter_by(id=user_id).first()
        if person:
            person.age = age
            db.session.commit()
            person_data = {
                'id': person.id,
                'name': person.name,
                'email': person.email,
                'gender': person.gender,
                'age': person.age
            }
            # Returns success message
            return jsonify({'message': 'Person updated successfully', 'person': person_data}), 200
        else:
            return jsonify({'message': 'Person not found or does not exist'}), 404

    # Returns an error if the request body key or value is absent
    except (KeyError, ValueError):
        db.session.rollback()
        return jsonify({'error': "Invalid request"}), 400

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    ''' This endpoint takes a DELETE request to delete a specific person in the database.
    
    Parameters:
        user_id (int): A parameter passed in the URL which value indicates the ID of the person to delete.

    Returns:
        JSON: A json response returns a message indicating if the task was successful or an error message.

    Example:
        DELETE /api/<user_id>
    '''
    try:
        # Input validation
        if not isinstance(user_id, int):
            return jsonify({'error': 'Invalid input data'}), 400
        
        person = Person.query.filter_by(id=user_id).first()
        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify({'message': 'Person deleted successfully'}), 200
        else:
            return jsonify({'message': 'Person not found or does not exist'}), 404

    # Returns an error if the request body key or value is absent
    except (KeyError, ValueError):
        db.session.rollback()
        return jsonify({'error': "Invalid request"}), 400

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)