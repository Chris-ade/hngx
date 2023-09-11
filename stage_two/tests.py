import requests
import json

# contains the base url of the app
base_url = 'http://localhost:5000/api'
user_data = {}

# Function to print the response and status code
def print_response(response):
    print(f'Status Code: {response.status_code}')
    print('Response:')
    print(response.json())

# Test the CREATE endpoint
def test_create_person():
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'johndoe@example.com',
        'gender': 'male'
    }
    response = requests.post(base_url, json=data)
    response_data = response.json()
    user_id = response_data.get('id')  # Get the ID from the response
    print('Testing CREATE endpoint:')
    print_response(response)
    # Returns the user ID
    return user_id 

# Test the GET endpoint
def test_get_person(user_id):
    response = requests.get(f'{base_url}/{user_id}')
    print(f'Testing GET endpoint for person ID: {user_id}')
    print_response(response)

# Test the UPDATE endpoint
def test_update_person(user_id):
    data = {
        'age': 21,
    }
    response = requests.put(f'{base_url}/{user_id}', json=data)
    print(f'Testing UPDATE endpoint for person ID: {user_id}')
    print_response(response)

# Test the DELETE endpoint
def test_delete_person(user_id):
    response = requests.delete(f'{base_url}/{user_id}')
    print(f'Testing DELETE endpoint for person ID: {user_id}')
    print_response(response)

if __name__ == '__main__':
    # Test CREATE endpoint
    user_id = test_create_person()

    # Test GET endpoint
    test_get_person(user_id)

    # Test UPDATE endpoint
    test_update_person(user_id)

    # Test DELETE endpoint
    test_delete_person(user_id)